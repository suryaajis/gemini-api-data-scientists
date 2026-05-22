# Session 2 — Resources

## Build an Interactive RAG Application with Gemini: A Step-by-Step Guide

**Source:** https://youtu.be/ozq9fK9Pn-s

---

## Overview

Video ini membahas cara membangun aplikasi **RAG (Retrieval-Augmented Generation)** menggunakan **Gemini API (free version)**, **ChromaDB** sebagai vector database, **LangChain** untuk text splitting, dan **Chainlit** untuk membangun user interface.

**Dua bagian utama:**
1. **Part 1 — Notebook:** Membangun RAG pipeline dari awal
2. **Part 2 — Interface:** Membangun UI interaktif dengan Chainlit

**Use case demo:** Chatbot yang hanya menjawab pertanyaan seputar **EMS (Environmental Management System)** — jika pertanyaan di luar topik, model menjawab `"out of context"`.

---

## Part 1 — RAG Notebook

### Libraries yang Digunakan
```bash
pip install google-generativeai langchain chromadb pdfminer.six chainlit python-dotenv
```

### RAG Pipeline (6 Steps)

```
1. Question
      ↓
2. Search ChromaDB for relevant documents
      ↓
3. Convert passages (list → string) = Context
      ↓
4. Create Prompt (question + context)
      ↓
5. Send prompt to Gemini
      ↓
6. Get Answer
```

---

### Step 1 — Setup API Key

Buat file `.env`:
```
GEMINI_API_KEY=your_api_key_here
```

```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

Cek embedding model yang tersedia:
```python
for m in genai.list_models():
    print(m.name)
# Gunakan: models/embedding-001
```

---

### Step 2 — Load Dataset (JSON atau PDF)

**Dari JSON (format Alpaca):**
```python
import json

with open("dataset.json", "r") as f:
    data = json.load(f)

documents = []
for entry in data:
    # Konversi dictionary → string
    text = " ".join(str(v) for v in entry.values())
    documents.append(text)

print(len(documents))       # contoh: 398 entries
print(type(documents[0]))   # <class 'str'>
```

**Dari PDF:**
```python
from pdfminer.high_level import extract_text

raw_text = extract_text("document.pdf")

def clean_extracted_text(text):
    # Hapus karakter tidak diinginkan
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text

clean_text = clean_extracted_text(raw_text)
print(len(clean_text))  # contoh: 800,000 characters
```

---

### Step 3 — Text Chunking dengan LangChain

PDF menghasilkan teks sangat panjang — tidak bisa langsung dimasukkan ke model sekaligus. Solusinya: **split menjadi chunk kecil**.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # ukuran tiap chunk (karakter)
    chunk_overlap=100     # overlap antar chunk agar konteks tidak putus
)

chunks = splitter.create_documents([clean_text])
print(len(chunks))  # contoh: 898 chunks

# Tambahkan chunks ke documents list
for chunk in chunks:
    documents.append(chunk.page_content)
```

> **Kenapa ada overlap?** Untuk menghindari informasi penting terpotong di awal/akhir sebuah chunk.

---

### Step 4 — Embedding dengan Gemini

Ubah dokumen teks menjadi **vector representation** menggunakan Gemini embedding model.

```python
def embed_function(documents, title="EMS Document"):
    embeddings = []
    for doc in documents:
        result = genai.embed_content(
            model="models/embedding-001",
            content=doc,
            task_type="retrieval_document",
            title=title
        )
        embeddings.append(result["embedding"])
    return embeddings
```

> **Tips:** Berikan `title` yang relevan dengan domain data untuk hasil embedding yang lebih akurat. Jika data mencakup banyak domain, ubah `title` untuk masing-masing domain.

Embedding model menghasilkan vektor dengan **768 dimensi** per dokumen.

---

### Step 5 — Simpan ke ChromaDB

```python
import chromadb

def create_chroma_db(documents, db_name, path="./chroma_db"):
    client = chromadb.PersistentClient(path=path)

    # Buat atau load database yang sudah ada
    try:
        db = client.get_collection(name=db_name)
    except:
        db = client.create_collection(name=db_name)

    # Loop dan tambahkan vector ke database
    import time
    for i, doc in enumerate(documents):
        embedding = embed_function([doc])[0]
        db.add(
            documents=[doc],
            embeddings=[embedding],
            ids=[str(i)]
        )
        time.sleep(1)  # Rate limit: free API = 60 requests/menit

    return db

db = create_chroma_db(documents, db_name="ems_database")
```

Cek isi database dengan pandas:
```python
import pandas as pd

data = db.get(include=["embeddings", "documents", "metadatas"])
df = pd.DataFrame({
    "id": data["ids"],
    "document": data["documents"],
    "embedding": data["embeddings"]
})
print(df.head())
# Setiap embedding memiliki 768 dimensi
```

---

### Step 6 — Query Vector Database

```python
def get_relevant_passages(question, db, n_results=5):
    query_embedding = genai.embed_content(
        model="models/embedding-001",
        content=question,
        task_type="retrieval_query"
    )["embedding"]

    results = db.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]  # list of relevant passages

passages = get_relevant_passages("What is ISO 14001?", db, n_results=5)
print(len(passages))  # 5 dokumen relevan
```

---

### Step 7 — Prompting Strategy

Video menunjukkan 4 variasi prompt — kualitas prompt sangat mempengaruhi hasil:

| Prompt | Perilaku Model |
|---|---|
| **Prompt 1 (Basic)** | Menjawab semua pertanyaan dari training data (tidak terbatas) |
| **Prompt 2 (Constrained)** | Hanya menjawab jika relevan dengan context — jika tidak, output `"out of context"` |
| **Prompt 3 (Flexible)** | Output `"out of context"` tapi tetap menjawab pertanyaan apapun |
| **Prompt 4 (Described)** | Tambahkan deskripsi domain di awal prompt untuk hasil lebih akurat |

**Prompt 2 (yang direkomendasikan):**
```python
def convert_passages_to_string(passages):
    return " ".join(passages)

def make_prompt(question, passages):
    context = convert_passages_to_string(passages)
    prompt = f"""
You are a helpful assistant that answers questions about EMS (Environmental Management System).
Use the following context to answer the question.
If the question is not related to the provided context, respond with "out of context".

Context:
{context}

Question: {question}

Answer:
"""
    return prompt
```

**Generate jawaban:**
```python
model = genai.GenerativeModel("gemini-2.5-flash")

question = "What is ISO 14001?"
passages = get_relevant_passages(question, db)
prompt = make_prompt(question, passages)

response = model.generate_content(prompt)
print(response.text)
```

---

## Part 2 — Chainlit Interface

### Cara Menjalankan Chainlit
```bash
chainlit run app.py -w
```
Flag `-w` = watch mode (auto-reload saat file berubah).

---

### Struktur `app.py`

```python
import chainlit as cl
import google.generativeai as genai
import chromadb
from dotenv import load_dotenv
import os

# ---- Konfigurasi default model ----
config = {
    "temperature": 0.9,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 2048
}

# ---- Setup API & Load Database ----
def setup_google_api():
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_vector_database():
    client = chromadb.PersistentClient(path="./chroma_db")
    db = client.get_collection(name="ems_database")
    return db

# ---- Dipanggil saat aplikasi pertama kali start ----
@cl.on_chat_start
async def start():
    setup_google_api()
    db = load_vector_database()

    # Simpan ke user session agar bisa diakses di method lain
    cl.user_session.set("db", db)

    # Buat model dengan konfigurasi awal
    model = genai.GenerativeModel(
        "gemini-2.5-flash",
        generation_config=config
    )
    cl.user_session.set("model", model)

    # Settings panel dengan slider
    settings = await cl.ChatSettings([
        cl.input_widget.Slider(id="temperature", label="Temperature", min=0, max=2, step=0.1, initial=0.9),
        cl.input_widget.Slider(id="top_p", label="Top P", min=0, max=1, step=0.05, initial=0.9),
        cl.input_widget.Slider(id="top_k", label="Top K", min=1, max=100, step=1, initial=40),
        cl.input_widget.Slider(id="max_output_tokens", label="Max Output Tokens", min=100, max=4096, step=100, initial=2048),
    ]).send()

# ---- Dipanggil saat user mengubah settings ----
@cl.on_settings_update
async def setup_model(new_settings):
    config["temperature"] = float(new_settings["temperature"])
    config["top_p"] = float(new_settings["top_p"])
    config["top_k"] = int(new_settings["top_k"])
    config["max_output_tokens"] = int(new_settings["max_output_tokens"])

    model = genai.GenerativeModel(
        "gemini-2.5-flash",
        generation_config=config
    )
    cl.user_session.set("model", model)

# ---- Dipanggil setiap kali user mengirim pesan ----
@cl.on_message
async def main(message: cl.Message):
    model = cl.user_session.get("model")
    db = cl.user_session.get("db")

    question = message.content
    passages = get_relevant_passages(question, db, n_results=5)
    prompt = make_prompt(question, passages)

    response = model.generate_content(prompt)
    await cl.Message(content=response.text).send()
```

---

### Fitur UI Chainlit

| Fitur | Keterangan |
|---|---|
| **New Chat** | Tombol untuk memulai percakapan baru |
| **Prompt History** | Riwayat prompt lengkap dengan tanggal |
| **Settings Panel** | Slider untuk Temperature, Top-P, Top-K, Max Tokens |
| **Attach Files** | Upload PDF atau CSV langsung dari UI |
| **Prompt Area** | Area input untuk mengetik pertanyaan |

---

## Key Concepts

### Mengapa RAG?
Model Gemini hanya tahu data yang digunakan untuk melatihnya. Dengan RAG, kita bisa memberikan **domain-specific knowledge** tanpa perlu fine-tuning — cukup simpan data ke vector database dan berikan sebagai konteks ke model.

### Mengapa ChromaDB?
ChromaDB adalah vector database yang ringan, bisa berjalan **lokal** (tanpa server), dan cocok untuk prototyping maupun production skala kecil-menengah.

### User Session di Chainlit
`cl.user_session` digunakan untuk menyimpan objek (model, database) agar tidak perlu di-load ulang setiap kali ada pesan baru — menjaga performa aplikasi tetap efisien.

### Rate Limit Free API
Gemini free API memiliki limit **60 requests per menit**. Saat mengisi ChromaDB dengan banyak dokumen, tambahkan `time.sleep(1)` di dalam loop embedding.

---

## Referensi Tambahan
- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [ChromaDB Docs](https://docs.trychroma.com/)
- [LangChain Text Splitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- [Chainlit Docs](https://docs.chainlit.io/)
