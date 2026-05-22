# Ringkasan Materi Sesi 2 — Implementasi RAG dengan LangChain

**Program:** LLM-Based Tools and Gemini API Integration for Data Scientists
**Penyelenggara:** Hacktiv8 — Maju Bareng AI

---

## Agenda Sesi 2

1. Pengenalan RAG (Retrieval-Augmented Generation)
2. Vector Database
3. Pengenalan LangChain
4. Pengenalan Llama

---

## 1. Pengenalan RAG

### Apa itu RAG?

RAG (Retrieval-Augmented Generation) adalah teknik yang menggabungkan dua proses utama:

- **Retrieval** — Mencari informasi relevan dari sumber eksternal (dokumen, database, dll.)
- **Generation** — Menggunakan LLM untuk menghasilkan respons berdasarkan informasi yang ditemukan

### Komponen RAG

| Komponen | Fungsi |
|---|---|
| **Retrieval Component** | Mencari dan mengambil dokumen relevan dari Vector Database berdasarkan query pengguna |
| **Augmented-Generation Component** | LLM yang menghasilkan jawaban dengan memanfaatkan dokumen yang telah diambil sebagai konteks |

### Alur Kerja RAG (7 Langkah)

```
1. User mengajukan pertanyaan
        ↓
2. Pertanyaan dikonversi menjadi vektor (embedding)
        ↓
3. Sistem melakukan pencarian di Vector Database
        ↓
4. Dokumen/data relevan diambil dari database
        ↓
5. Dokumen relevan dikirim ke LLM bersama pertanyaan
        ↓
6. LLM memproses konteks dan menghasilkan jawaban
        ↓
7. Output/jawaban diberikan ke user
```

### Manfaat RAG

1. **Improved Accuracy** — Jawaban lebih akurat karena didasarkan pada dokumen nyata
2. **Access to Up-to-Date Information** — Tidak perlu melatih ulang model; cukup perbarui database
3. **Enhanced Contextual Understanding** — Model memahami konteks spesifik domain/bisnis
4. **Increased Transparency** — Sumber referensi bisa dilacak dan diverifikasi
5. **Customization** — Mudah dikustomisasi untuk kebutuhan spesifik
6. **Reduced Training Costs** — Hemat biaya karena tidak perlu fine-tuning model

### Keunggulan Utama RAG

- Mengurangi **hallucination** (jawaban yang salah/tidak berdasar)
- Informasi bisa diperbarui **real-time** tanpa retraining
- Implementasi chatbot yang lebih **cepat dan murah**

---

## 2. Vector Database

### Apa itu Vector Database?

Vector Database adalah sistem yang dioptimalkan khusus untuk menyimpan, mengelola, dan melakukan pencarian data dalam bentuk vektor (representasi numerik dari teks, gambar, audio, dll.).

### Komponen Vector Database

| Komponen | Contoh | Fungsi |
|---|---|---|
| **Embedding Model** | BERT, CLIP, Whisper | Mengonversi data mentah menjadi vektor |
| **Indexing Mechanism** | HNSW, IVF-PQ, ANNOY | Mengorganisir vektor untuk pencarian cepat |
| **Similarity Metrics** | Cosine Similarity, Euclidean Distance | Mengukur kemiripan antar vektor |
| **Storage Engine** | — | Menyimpan data vektor secara efisien |

### Contoh Vector Database

**Open Source:**
- Faiss (Meta)
- Chroma
- Qdrant
- CockroachDB

**Enterprise / Cloud:**
- Elastic Search
- Azure AI Search
- Vertex AI (Google)
- Pinecone

### Use Case Vector Database

- **RAG** — Pencarian dokumen untuk augmentasi LLM
- **Image/Product Search** — Pencarian gambar atau produk berdasarkan kemiripan visual
- **Search Engines** — Mesin pencari semantik yang memahami makna, bukan hanya kata kunci

---

## 3. LangChain

### Apa itu LangChain?

LangChain adalah framework untuk membangun aplikasi berbasis LLM. LangChain menghubungkan berbagai komponen:

```
Model  →  Prompt  →  Chain  →  Memory
```

### Manfaat LangChain

1. **Integrasi Mudah dengan Berbagai LLM**
   - Menyediakan kode yang konsisten untuk berbagai model bahasa
   - Mudah menguji dan mengimplementasikan model yang berbeda tanpa perubahan kode signifikan

2. **Pengembangan Aplikasi AI yang Lebih Cepat**
   - Komponen modular seperti Prompt Templates dan Chains
   - Membangun dan menguji prototipe aplikasi AI lebih efisien

3. **Fleksibilitas dalam Integrasi Data**
   - Menghubungkan LLM dengan sumber data eksternal
   - Respons lebih relevan dan ter-update

### Komponen Dasar: Prompt Template

**Apa itu Prompt Template?**
Komponen yang membantu developer membuat pola teks dengan placeholder (penanda) untuk input yang dinamis.

**Manfaat Prompt Template:**
- Menjaga konsistensi instruksi ke model
- Memudahkan penggunaan ulang pola yang sama
- Mengontrol format output

**Contoh Kode:**
```python
from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following from {language_from} into {language_to}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({
    "language_from": "Indonesian",
    "language_to": "Italian",
    "text": "Saya saat ini sedang belajar generative AI"
})
```

---

## 4. Llama

### Apa itu Llama?

**Llama** (Large Language Model Meta AI) adalah LLM yang dirancang oleh **Meta** dengan karakteristik:

- Efisien dan berorientasi pada penelitian
- Tersedia dalam berbagai ukuran model (menyesuaikan kebutuhan dan sumber daya)
- **Open Source** — siapa saja bisa mengaksesnya secara gratis

### Kegunaan Llama

Sama seperti LLM lain pada umumnya:
- Text generation
- Summarization
- Code generation
- Dan lainnya

### Setup Llama via Groq Cloud

Llama dapat diakses melalui **Groq Cloud** sebagai inference provider:

1. Buka [https://console.groq.com/](https://console.groq.com/)
2. Login dengan akun yang sudah dibuat
3. Di sidebar, pilih **API Keys** → **Create API Key**
4. Simpan API Key di tempat aman (hanya bisa diakses sekali)
5. Gunakan API Key tersebut untuk mengakses Llama dari environment Python

> Dokumentasi: [https://console.groq.com/docs/quickstart](https://console.groq.com/docs/quickstart)

### Parameter Tuning Llama

Parameter yang digunakan Llama sama seperti LLM lain:

| Parameter | Fungsi |
|---|---|
| **Temperature** | Mengontrol kreativitas output. Nilai tinggi = lebih kreatif/variatif |
| **Max Tokens** | Membatasi jumlah token dalam satu output. Jika terlalu kecil, output bisa terpotong |
| **Top-p (Nucleus Sampling)** | Alternatif dari temperature; membatasi pemilihan kata dari probabilitas tertinggi |
| **Frequency Penalty** | Mencegah pengulangan kata/frasa berlebihan. Nilai tinggi = lebih variatif |
| **Presence Penalty** | Mendorong model menyebutkan kata-kata baru yang belum muncul dalam respons |

> **Catatan:** Top-p dan Temperature memiliki fungsi yang sama — cukup pilih salah satu untuk digunakan.

---

## 5. Hands-On: Implementasi RAG

Notebook praktik tersedia di Google Colab (duplicate ke Drive pribadi):

- **RAG dengan Llama** (via Groq Cloud)
- **RAG dengan Gemini** (via Google AI Studio)

**Persiapan sebelum hands-on:**
- Akun Groq: [https://console.groq.com/](https://console.groq.com/)
- Gemini API Key: [https://aistudio.google.com/](https://aistudio.google.com/)
- 1 dokumen PDF (2–5 halaman) sebagai knowledge base chatbot

---

## Ringkasan Konsep

```
Dokumen PDF/Data
      ↓ (Embedding Model)
Vector Database (ChromaDB / Faiss / Pinecone)
      ↓ (Semantic Search)
Dokumen Relevan
      ↓ (LangChain Chain)
LLM (Gemini / Llama) + Konteks
      ↓
Jawaban yang Akurat & Relevan
```

| Teknologi | Peran |
|---|---|
| **LangChain** | Framework untuk membangun pipeline RAG |
| **ChromaDB / Faiss** | Menyimpan vektor dokumen |
| **Embedding Model** | Mengonversi teks → vektor |
| **Gemini API** | LLM untuk generating respons |
| **Llama via Groq** | Alternatif LLM open source gratis |
| **Prompt Template** | Menjaga konsistensi instruksi ke LLM |

---

## Preview Sesi 3

Di Sesi 3, kita akan membangun **tampilan chatbot** berbasis web menggunakan Streamlit — dari RAG pipeline yang sudah dibangun di Sesi 2 menjadi aplikasi chatbot yang bisa diakses via browser.
