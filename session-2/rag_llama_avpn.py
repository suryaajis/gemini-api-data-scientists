# RAG (Retrieval-Augmented Generation) dengan LangChain & LangGraph
#
# Sebelum menjalankan, buat file .env di folder ini dengan isi:
#   GOOGLE_API_KEY=your_gemini_api_key
#   GROQ_API_KEY=your_groq_api_key
#
# Install dependencies: pip install -r requirements.txt

from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────────
# PART 1: Vector Database dengan FAISS
# ─────────────────────────────────────────────

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    output_dimensionality=768
)

index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

# ── Tambah Dokumen ke Vector Store ──────────────
from uuid import uuid4
from langchain_core.documents import Document

documents = [
    Document(page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.", metadata={"source": "tweet"}),
    Document(page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.", metadata={"source": "news"}),
    Document(page_content="Building an exciting new project with LangChain - come check it out!", metadata={"source": "tweet"}),
    Document(page_content="Robbers broke into the city bank and stole $1 million in cash.", metadata={"source": "news"}),
    Document(page_content="Wow! That was an amazing movie. I can't wait to see it again.", metadata={"source": "tweet"}),
    Document(page_content="Is the new iPhone worth the price? Read this review to find out.", metadata={"source": "website"}),
    Document(page_content="The top 10 soccer players in the world right now.", metadata={"source": "website"}),
    Document(page_content="LangGraph is the best framework for building stateful, agentic applications!", metadata={"source": "tweet"}),
    Document(page_content="The stock market is down 500 points today due to fears of a recession.", metadata={"source": "news"}),
    Document(page_content="I have a bad feeling I am going to get deleted :(", metadata={"source": "tweet"}),
]

uuids = [str(uuid4()) for _ in range(len(documents))]
vector_store.add_documents(documents=documents, ids=uuids)

# ── Similarity Search ────────────────────────────
results = vector_store.similarity_search(
    "LangChain provides abstractions to make working with LLMs easy",
    k=2,
    filter={"source": {"$eq": "tweet"}},
)
print("=== Search dengan filter source=tweet ===")
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")

results = vector_store.similarity_search("The new iPhone", k=2)
print("\n=== Search tanpa filter ===")
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")

# ── Simpan & Muat FAISS Index ────────────────────
vector_store.save_local("faiss_index")
print("\nIndex tersimpan di folder faiss_index/")

new_vector_store = FAISS.load_local(
    "faiss_index", embeddings, allow_dangerous_deserialization=True
)
docs = new_vector_store.similarity_search("qux")
print("\n=== Reload dari disk ===")
for res in docs:
    print(f"* {res.page_content} [{res.metadata}]")


# ─────────────────────────────────────────────
# PART 2: RAG Pipeline dengan LangChain & LangGraph
# ─────────────────────────────────────────────

from langchain_text_splitters import CharacterTextSplitter
import fitz  # PyMuPDF

# ── Langkah 1: Extract dan Chunk Dokumen ────────
def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])

# Ganti path ini dengan PDF kamu
PDF_PATH = "docs/Rizky_Andika_CV.pdf"
pdf_text = extract_text_from_pdf(PDF_PATH)
print(f"\nTotal karakter: {len(pdf_text)}")
print("Preview 500 karakter pertama:")
print(pdf_text[:500])

splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_text(pdf_text)
print(f"\nTotal chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk[:100]}...")

# ── Langkah 2: Upload Chunk ke Vector Store ─────
index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

documents = [Document(page_content=chunk) for chunk in chunks]
uuids = [str(uuid4()) for _ in range(len(documents))]
vector_store.add_documents(documents=documents, ids=uuids)
print(f"\n{len(documents)} chunks berhasil disimpan ke vector store")

vector_store.save_local("faiss_index")
print("Index tersimpan di folder faiss_index/")

# ── Langkah 3: Bangun RAG dengan LangGraph ──────
from typing import List, TypedDict
from langchain_groq import ChatGroq
from langchain import hub
from langgraph.graph import START, StateGraph

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

prompt = hub.pull("rlm/rag-prompt")

llm = ChatGroq(
    temperature=0,
    model="llama-3.3-70b-versatile",
)

def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}

graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()
print("\nGraph berhasil dikompilasi!")

# ── Jalankan RAG ─────────────────────────────────
result = graph.invoke({"question": "Who is Rizky Andika?"})

print("\n=== Context yang diambil dari FAISS ===")
for i, doc in enumerate(result["context"]):
    print(f"\nChunk {i+1}:")
    print(doc.page_content[:200] + "...")

print("\n=== Jawaban LLM ===")
print(result["answer"])

result2 = graph.invoke({"question": "When and where is Rizky Andika graduated?"})
print(f'\nAnswer: {result2["answer"]}')
