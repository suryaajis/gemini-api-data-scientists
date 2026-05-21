# Ringkasan Materi Sesi 1
## LLM-Based Tools & Gemini API Integration for Data Scientists
**Program: Maju Bareng AI — Hacktiv8**
> Didukung oleh Google.org dan Asian Development Bank

---

## Informasi Program

| Atribut | Detail |
|---|---|
| Nama Program | Maju Bareng AI |
| Penyelenggara | Hacktiv8 (PT. Hacktivate Teknologi Indonesia) |
| Durasi | 1 minggu per batch |
| Platform | Online — Google Classroom & Google Meet |
| Total Sesi | 3 Sesi |
| Total Durasi | 10 Jam |

### Struktur 3 Sesi

| Sesi | Topik |
|---|---|
| Sesi 1 | Pengantar AI & Implementasi Generative AI dengan Gemini |
| Sesi 2 | Implementasi RAG dengan LangChain |
| Sesi 3 | Pembuatan Chatbot dengan LLM (Streamlit + Deploy ke Cloud) |

### Program Timeline
- **Week 1 (Sun):** Self Learning Session 1
- **Week 2 (Mon):** Online Session 1 — 19.00–22.00 WIB
- **Week 2 (Tue):** Self Learning Session 2
- **Week 2 (Wed):** Online Session 2 — 19.00–22.00 WIB
- **Week 2 (Thu):** Self Learning Session 3
- **Week 2 (Fri):** Online Session 3 — 19.00–22.00 WIB
- **Week 2 (Sun):** Final Project Submission

### Checklist Tugas

| Phase | Task | Due Date |
|---|---|---|
| Session 1 | Pre-Test + Presence & Quiz 1 | Session 1 |
| Session 2 | Presence & Quiz 2 | Session 2 |
| Session 3 | Presence & Quiz 3 + Post-Test | Session 3 |
| Final Project | Form Submission | H+2 Session 3 |

### Syarat Mendapat Sertifikat

| | Presence | Pre-Post Survey | Quiz | Final Project |
|---|---|---|---|---|
| **Tier 1** | 2/3 | 2/2 | 3/3 | 1/1 (wajib) |
| **Tier 2** | 2/3 | 2/2 | 3/3 | 0/1 |

---

## Agenda Sesi 1

1. Konsep AI & Generative AI serta Etika
2. Pengenalan Chatbot
3. Halusinasi dan Teknik Prompting Dasar
4. Pengenalan Gemini
5. Generasi Teks dari Berbagai Jenis Input
6. Teknik Prompting Lanjutan
7. Konfigurasi Google Gemini
8. Function Calling

### Prerequisites (Training Guidelines)
- Pengetahuan dasar **Python, Machine Learning, dan NLP**
- Materi sebagian besar bersifat praktik menggunakan **Google Colab (Jupyter Notebook)**

### Learning Objectives
- Memahami definisi AI, Generative AI, dan LLM
- Menguasai teknik dasar dan lanjutan dalam prompting
- Memahami cara kerja Chatbot berbasis LLM
- Menggunakan Function Calling pada Google Gemini
- Menerapkan konfigurasi parameter pada Google Gemini

---

## 1. Pengenalan AI, Generative AI, dan LLM

### Definisi Artificial Intelligence (AI)
AI adalah bidang ilmu yang berkaitan dengan pembuatan komputer dan mesin yang dapat bernalar, belajar, dan bertindak layaknya kecerdasan manusia.

**Evolusi AI:**
```
1950s → AI (Human intelligence exhibited by machines)
1980s → Machine Learning (AI systems that learn from historical data)
2010s → Deep Learning (Machine learning models mirroring human brain)
2020s → Generative AI (Foundation models that create original content)
```

### Cabang-Cabang Utama AI
- **Machine Learning** — Belajar dari data untuk membuat prediksi (contoh: rekomendasi produk)
- **Computer Vision** — Memberi kemampuan "melihat" pada mesin (contoh: face unlock)
- **Natural Language Processing (NLP)** — Membuat mesin paham bahasa manusia (contoh: Google Assistant)
- **Robotics** — Memberi AI bentuk fisik untuk berinteraksi dengan dunia

### Generative AI
Generative AI adalah AI yang bisa menghasilkan konten baru seperti teks, gambar, musik, atau video berdasarkan data yang telah dipelajari sebelumnya, menggunakan teknik **Deep Learning** dan arsitektur **neural network** besar.

**Manfaat Generative AI:**
- **Kreativitas** — Membantu seniman, desainer, penulis menghasilkan ide baru
- **Otomatisasi** — Mempercepat pembuatan konten (artikel, gambar, musik)
- **Aksesibilitas** — Memungkinkan siapa saja membuat sesuatu yang kreatif tanpa keahlian teknis
- **Pendidikan** — Menciptakan materi edukasi yang interaktif dan personal

### Perbandingan Model Gen AI Terkini

| Company | Model |
|---|---|
| OpenAI | GPT-5 mini, GPT-5 |
| Meta | LLaMA 4 Maverick, LLaMA 4 Scout |
| Google | Gemini 2.5 Pro, Gemini 2.5 Flash |
| Anthropic | Claude 4.1 Opus, Claude 4.0 Sonnet |
| XAi | Grok 4 |

### Large Language Model (LLM)
LLM adalah program komputer yang mempelajari dan menghasilkan bahasa menyerupai bahasa manusia menggunakan arsitektur **transformer** yang dilatih pada data dalam jumlah sangat besar.

**Karakteristik LLM:**
- Dibangun menggunakan transformer (encoder + decoder + self-attention)
- Sangat fleksibel — satu model dapat menjawab pertanyaan, meringkas, menerjemahkan
- Dapat digunakan dalam aplikasi Generative AI melalui prompt

**Aplikasi LLM di Berbagai Industri:**

| Industri | Aplikasi |
|---|---|
| Teknologi | Chatbot, Virtual Assistant (Siri, Alexa), Pencarian Informasi |
| Media & Penerbitan | Pembuatan konten otomatis, analisis sentimen |
| E-Commerce | Rekomendasi produk, penerjemahan multibahasa |
| Kesehatan | Analisis teks medis, chatbot konsultasi kesehatan |

**Tantangan dan Keterbatasan LLM:**
- **Data yang memadai** — Membutuhkan data pelatihan sangat besar
- **Bias dalam model** — Data bias menghasilkan output yang tidak akurat atau diskriminatif
- **Kompleksitas dan biaya** — Komputasi tinggi, mahal untuk model besar
- **Konteks yang dalam** — Kesulitan memahami konteks yang lebih luas atau spesifik

---

## 2. Etika AI

### Definisi
Etika AI adalah seperangkat prinsip moral dan nilai-nilai yang memandu pengembangan, penerapan, dan penggunaan AI secara bertanggung jawab, untuk menjawab pertanyaan:
> **"Bagaimana kita memastikan AI melayani kita dengan adil, aman, dan tanpa merugikan?"**

### Prinsip Utama Etika AI

| Prinsip | Penjelasan | Analogi |
|---|---|---|
| Transparansi | Pengguna perlu tahu apa yang dilakukan AI dan alasannya | Seperti kalkulator: anda tahu rumus di balik perhitungannya |
| Keadilan | AI harus memperlakukan semua pengguna secara adil | Seperti wasit yang adil dalam permainan |
| Akuntabilitas | Manusia — bukan mesin — yang bertanggung jawab atas hasil AI | Seperti koki yang bertanggung jawab atas masakan |
| Privasi | Data pribadi harus dilindungi dan hanya digunakan dengan persetujuan | Seperti buku harian yang terkunci |
| Keamanan | AI tidak boleh menimbulkan bahaya secara sengaja maupun tidak | Seperti merancang mobil dengan rem dan airbag |

### Rekomendasi UNESCO (2021)
UNESCO menghasilkan standar global pertama tentang etika AI. Inti rekomendasinya:
1. Hak Asasi & Martabat Manusia
2. Masyarakat damai, adil, saling terhubung
3. Keanekaragaman & Inklusivitas
4. Lingkungan & Ekosistem yang Berkelanjutan

### 10 Prinsip HAM Terhadap AI
1. Proporsionalitas dan Tidak Menimbulkan Kerugian
2. Keselamatan dan Keamanan
3. Hak Privasi dan Perlindungan Data
4. Tata Kelola & Kolaborasi Multi-Pemangku Kepentingan dan Adaptif
5. Tanggung Jawab dan Akuntabilitas
6. Transparansi dan Kejelasan
7. Pengawasan dan Penentuan Manusia
8. Keberlanjutan
9. Kesadaran & Literasi
10. Keadilan dan Non-Diskriminasi

---

## 3. Pengenalan Chatbot

### Definisi
Chatbot adalah program komputer yang dirancang untuk mensimulasikan percakapan manusia melalui teks atau suara.

**Dua Jenis Chatbot:**

| | AI Chatbot | Rule-Based Chatbot |
|---|---|---|
| **Kelebihan** | Menggunakan NLP, user bebas menulis pertanyaan, berkembang sendiri | Implementasi sederhana, dapat menjawab pertanyaan umum |
| **Kekurangan** | Investasi awal besar, butuh chat history, setup kompleks | Tidak bisa selesaikan pertanyaan kompleks, tidak paham sinonim |

### Teknologi di Balik Chatbot
- **NLP** — Memahami, memproses, dan merespons teks atau suara manusia
- **Machine Learning** — Meningkatkan kemampuan respons dari data interaksi sebelumnya
- **LLM** — Model machine learning yang dilatih pada dataset teks sangat besar

### Cara Kerja AI Chatbot
```
User → [Natural Language Question]
     → Chatbot Platform
     → NLP (Language Parsing)
     → Knowledge Base / Data Storage
     → Response Generation
     → [Natural Language Answer] → User
```

---

## 4. Halusinasi dan Teknik Prompting

### Halusinasi pada Chatbot
Halusinasi terjadi ketika chatbot berbasis LLM menghasilkan **jawaban yang salah, tidak akurat, atau sepenuhnya fiktif** meskipun tampak meyakinkan.

**Penyebab Halusinasi:**
- Model tidak memiliki pengetahuan dunia nyata yang cukup
- Data training yang tidak memadai
- Ketergantungan pada pola teks
- Overfitting pada data latihan
- Tidak ada mekanisme verifikasi fakta
- Konteks prompt yang tidak jelas

### Prompting
Prompt adalah input atau perintah yang diberikan pengguna untuk mendapatkan respons dari model.

**Good Prompt vs Bad Prompt:**
- **Good:** Clear, Specific, Has enough context, Contains audience insights
- **Bad:** Vague, Generic, Has little to no context, Doesn't have details

### Teknik Dasar Prompting

| Teknik | Deskripsi | Contoh |
|---|---|---|
| **Zero-Shot** | Model menyelesaikan tugas tanpa contoh sebelumnya | *"Jelaskan bagaimana cara kerja mesin uap."* |
| **One-Shot** | Model diberikan satu contoh sebelum diminta melakukan tugas | *"Contoh: 3 + 2 = 5. Sekarang, berapa 4 + 6?"* |
| **Few-Shot** | Model diberikan beberapa contoh (2–5) sebelum melakukan tugas | Contoh HTML, CSS lalu tanya JavaScript |
| **Instructional** | Instruksi jelas dan terperinci dengan langkah-langkah spesifik | *"Tulis esai... dimulai dengan... diikuti... akhiri dengan..."* |
| **Priming (Contextual)** | Memberikan konteks/informasi awal yang relevan | Memberikan setting cerita sebelum bertanya |
| **Role-Based** | Meminta model menjawab dengan peran tertentu | *"Sebagai seorang dokter, apa yang harus dilakukan..."* |
| **Comparative** | Meminta model membandingkan dua atau lebih hal | *"Bandingkan energi terbarukan dan fosil..."* |

---

## 5. Pengenalan Gemini

### Apa Itu Gemini?
Gemini (sebelumnya dikenal sebagai Bard) adalah chatbot AI generatif yang dikembangkan oleh Google. Dirancang dengan kemampuan **multimodal** — dapat memahami dan mengolah teks, kode, audio, gambar, dan video.

### Gemini API
Gemini API memungkinkan akses ke model generatif terbaru Google untuk berbagai tugas:
- **Gemini Flash** — Dioptimalkan untuk kecepatan dan efisiensi, respons cepat
- **Gemini Pro** — Model lebih besar dan kuat untuk tugas kompleks yang membutuhkan penalaran dalam
- **Model Lainnya** — Text embedding, AQA, dll.

### Cara Mendapatkan API Key
1. Kunjungi **Google AI Studio**
2. Pilih **Get API Key**
3. Klik **Create API Key**

---

## 6. Teknik Prompting Lanjutan

### Chain-of-Thought (CoT)
Diperkenalkan oleh Wei et al. (2022). CoT memungkinkan penalaran kompleks melalui langkah-langkah penalaran menengah.

- **Zero-shot CoT:** Tambahkan *"Let's think step by step"* pada prompt
- **Few-shot CoT:** Berikan beberapa contoh penalaran sebelum pertanyaan utama

**Keunggulan CoT:** Meningkatkan akurasi pada soal matematika, logika, dan penalaran multi-langkah.

### Tree of Thoughts (ToT)
Diusulkan oleh Yao et al. (2023). ToT memperluas konsep CoT dengan eksplorasi beberapa jalur penalaran sekaligus, layaknya pohon keputusan.

**Contoh prompt ToT:**
> *"Imagine three different experts are answering this question. All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realises they're wrong at any point then they leave. The question is..."*

### ReAct (Reason + Act)
Diperkenalkan oleh Yao et al. (2022). ReAct mengombinasikan **reasoning traces** dan **action steps**:
- **Reasoning traces** — Model membuat, melacak, dan memperbarui rencana tindakan
- **Action step** — Model berinteraksi dengan sumber eksternal (knowledge base, environment)

ReAct mengatasi kelemahan CoT yang tidak dapat mengakses dunia luar atau memperbarui pengetahuannya.

### Teknik Lainnya
- Self-Consistency
- Automatic Reasoning and Tool-use (ART)
- Reflexion
- Directional Stimulus Prompting
- Referensi lengkap: https://www.promptingguide.ai/techniques

---

## 7. Konfigurasi Google Gemini

Setiap request ke model Gemini menyertakan parameter yang dikontrol melalui `GenerationConfig`.

### Parameter Utama

#### Temperature
- Mengontrol tingkat keacakan dan kreativitas output
- Rentang nilai: **0 – 2**
- **Tinggi** → Output lebih beragam dan kreatif (tapi bisa kurang relevan)
- **Rendah / 0** → Output deterministik, selalu memilih probabilitas tertinggi

#### Max Output Tokens
- Menentukan jumlah token maksimum dalam respons
- 1 token ≈ 4 karakter
- 100 token ≈ 60–80 kata bahasa Inggris

#### Top-K
- Mengambil sampel dari K token dengan probabilitas tertinggi
- Rentang: **1–100**
- Top-K = 1 → hanya ambil token terbaik (Greedy Decoding, kurang kreatif)

#### Top-P
- Mengambil sampel token hingga akumulasi probabilitas mencapai nilai P
- Rentang: **0–1**
- Misal Top-P = 0.96 → ambil token sampai probabilitas kumulatif > 96%

---

## 8. Function Calling

### Definisi
Function calling adalah teknik yang memungkinkan LLM (seperti Gemini atau LLaMA) **berinteraksi dengan sistem eksternal** (API, database, dll.) dengan menghasilkan output terstruktur.

### Manfaat Function Calling
| Sebelum | Sesudah |
|---|---|
| LLM hanya bisa memberikan informasi, manusia yang melakukan aksinya | LLM dapat langsung melakukan aksi nyata berdasarkan input pengguna |

### Contoh Implementasi
- **Virtual Assistant** — Membuka aplikasi, memutar lagu, set alarm hanya dengan perintah teks
- **Chatbot Perusahaan** — Pengecekan data customer, melakukan transaksi langsung dari chat

### Alur Function Calling
```
User Query → LLM → Identify Function to Call
          → Generate Structured Arguments
          → Call External API/Database
          → Return Result to LLM
          → Generate Final Response for User
```

---

## Hands-On Praktik

### Hands-On 1: Text Generation dari Berbagai Input
Menggunakan Gemini API dengan Python untuk menghasilkan teks dari berbagai macam input.

### Hands-On 2: Konfigurasi Parameter
Bereksperimen dengan parameter `temperature`, `top_k`, `top_p`, dan `max_output_tokens` menggunakan Python dan Google Colab.

---

## Tools yang Dibutuhkan

| No | Tool | Versi | Sesi |
|---|---|---|---|
| 1 | Python Miniconda | 3.11–3.13.5 | 1–4 |
| 2 | Visual Studio Code | Latest | 1–4 |

**VS Code Extensions yang diinstall:**
- Python
- Jupyter Notebook

---

## Persiapan Sesi 2
Di Sesi 2, kita akan **membangun Chatbot sendiri** menggunakan RAG (Retrieval-Augmented Generation) dengan LangChain dan Vector Database.
