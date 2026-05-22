# Ringkasan Materi — Sesi 3
## Pembuatan Chatbot dengan Large Language Model (LLM)

**Program:** LLM-Based Tools and Gemini API Integration for Data Scientists  
**Penyelenggara:** Hacktiv8  
**Didukung oleh:** Google.org, AVPN, dan Asian Development Bank (AI Opportunity Fund: Asia Pacific)

---

## Struktur Keseluruhan Program

| Sesi | Topik | Subtopik |
|---|---|---|
| **Sesi 1** | Pengantar AI & Generative AI dengan Gemini | Konsep AI & Etika, Chatbot, Prompting, Gemini, Function Calling |
| **Sesi 2** | Implementasi RAG dengan LangChain | RAG, Vector Database, LangChain |
| **Sesi 3** | Pembuatan Chatbot dengan LLM | Membangun Chatbot dengan Streamlit, Deploy ke Cloud |

---

## Agenda Sesi 3

1. Membangun Chatbot Berbasis LLM dengan Streamlit
2. Mendeploy Aplikasi Streamlit ke Cloud

---

## Bagian 1 — Streamlit

### Apa itu Streamlit?

**Streamlit** adalah framework open-source berbasis Python yang memudahkan pengembang dalam membangun aplikasi web interaktif, khususnya di bidang **sains data** dan **machine learning** — tanpa perlu menguasai HTML, CSS, atau JavaScript.

### Mengapa Menggunakan Streamlit?

| Keunggulan | Penjelasan |
|---|---|
| **Open-Source Python Library** | Perkembangan komunitas yang sangat cepat |
| **Interactive User Interfaces** | Membangun tampilan web interaktif tanpa keahlian front-end |
| **Low-Code Development** | Membangun website dengan minimal coding |
| **Extensive Compatibility** | Terintegrasi dengan pandas, scikit-learn, LangChain, dll. |

### Memulai Streamlit

- Buat akun di [https://share.streamlit.io/](https://share.streamlit.io/) untuk deployment
- Install: `pip install streamlit`
- Jalankan: `streamlit run app.py`

### Widget Utama Streamlit

**Chart Widgets**
```python
st.area_chart(my_data_frame)   # Area chart
st.bar_chart(my_data_frame)    # Bar chart
st.line_chart(my_data_frame)   # Line chart
```

**Chat Widgets** (untuk membangun chatbot)
```python
prompt = st.chat_input("Say something")
with st.chat_message("user"):
    st.write("Hello!")
with st.status('Running'):
    do_something_slow()
```

**Status Widgets**
```python
st.progress(i)                        # Progress bar
with st.spinner("Please wait..."):    # Spinner
    do_something_slow()
with st.status('Running'):            # Status container
    do_something_slow()
```

---

## Bagian 2 — Streamlit for Chatbot

Hands-on membangun chatbot menggunakan Streamlit yang diintegrasikan dengan LLM via GitHub/Google Colab.

**Notebook:** [Google Colab — Streamlit for Chatbot](https://colab.research.google.com/drive/1eCrr13whf3l1FleL7KbAG9emDEfN_1Za?usp=sharing)

> Jangan lupa untuk **duplicate** Notebooknya ke Drive kamu ya!

---

## Bagian 3 — AI Agents

### Apa itu AI Agents?

**AI Agent** adalah program perangkat lunak yang dapat:
- Berinteraksi dengan lingkungannya secara mandiri
- Mengumpulkan data dari berbagai sumber
- Membuat keputusan dan menjalankan fungsi (tools/function calling) secara otomatis untuk mencapai tujuan yang telah ditetapkan

AI Agents pada dasarnya adalah **sekumpulan Tools (function calling)** yang dapat langsung membuat keputusan dan menjalankan fungsi yang diberikan.

### AI Agents vs AI Assistant

| | AI Agents | AI Assistant |
|---|---|---|
| **Tujuan** | Secara otomatis melakukan task sesuai tools yang diberikan | Menyarankan user melakukan tugasnya |
| **Kemampuan** | Bisa melakukan task rumit (misal: menghitung pengeluaran bulan lalu) | Hanya memberikan informasi (misal: cara cek saldo di ATM) |
| **Interaksi** | **Proactive** — goal-oriented | **Reactive** — responds to user requests |

### Contoh Use Case AI Agents

| Use Case | Deskripsi |
|---|---|
| **Data Agent** | Menganalisis data untuk menjawab pertanyaan user (misal: total customer minggu lalu, produk terjual) |
| **Customer Service Agent** | Menyelesaikan keluhan pelanggan dan langsung mengambil tindakan atas keluhan tersebut |
| **Code Agents** | Membantu developer menyusun kode lebih rapi dan memperbaiki bugs |

### Hands-On AI Agent

**Notebook:** [Google Colab — AI Agent](https://colab.research.google.com/drive/1enyklVQdzVbzFP9yc4iVErxzqF3Vy4-W?usp=sharing)

> Jangan lupa untuk **duplicate** Notebooknya ke Drive kamu ya!

---

## Quiz 3

- **Due Date:** Hari sesi berlangsung, pukul 23.59 WIB
- **Link:** [https://bit.ly/quiz3-data](https://bit.ly/quiz3-data)
- Pengisian quiz juga dihitung sebagai **absensi**

---

## Final Project

### Deskripsi

Buatlah sebuah **chatbot berbasis AI** dengan use case dan konfigurasi parameter yang sesuai dengan kreativitas masing-masing. Chatbot harus menggunakan model AI (NLP/LLM) untuk memproses bahasa alami dan memberikan respons yang relevan kepada pengguna.

### Contoh Use Case

- Customer service bot
- Education bot
- Travel assistant
- Personal productivity assistant

### Contoh Parameter Kreatif

- Gaya bahasa (formal / santai)
- Domain pengetahuan tertentu (kesehatan, edukasi, hobi)
- Integrasi API eksternal
- Fitur tambahan seperti memory dan rekomendasi

### Deliverables

- URL repositori GitHub
- Screenshots User Interface

**Due Date:** H+2 Sesi 3, pukul 23.59 WIB  
**Link Submit:** [https://bit.ly/finalproject-data](https://bit.ly/finalproject-data)

---

## Post-Test

1. Isi form Post-Survey: [https://bit.ly/mba2-postsurvey](https://bit.ly/mba2-postsurvey)
2. Screenshot bukti penyelesaian Post-Survey
3. Submit bukti ke link Post-Test: [https://bit.ly/posttest-data-ai](https://bit.ly/posttest-data-ai)
4. Lanjutkan mengisi Post-Test sampai selesai

---

## Referensi & Link Penting

| Resource | Link |
|---|---|
| Absensi | [https://bit.ly/absensi-data](https://bit.ly/absensi-data) |
| Notebook Streamlit Chatbot | [Google Colab](https://colab.research.google.com/drive/1eCrr13whf3l1FleL7KbAG9emDEfN_1Za?usp=sharing) |
| Notebook AI Agent | [Google Colab](https://colab.research.google.com/drive/1enyklVQdzVbzFP9yc4iVErxzqF3Vy4-W?usp=sharing) |
| Quiz 3 | [https://bit.ly/quiz3-data](https://bit.ly/quiz3-data) |
| Final Project Submit | [https://bit.ly/finalproject-data](https://bit.ly/finalproject-data) |
| Post-Survey | [https://bit.ly/mba2-postsurvey](https://bit.ly/mba2-postsurvey) |
| Post-Test | [https://bit.ly/posttest-data-ai](https://bit.ly/posttest-data-ai) |
| Streamlit Cheat Sheet | [https://cheat-sheet.streamlit.app/](https://cheat-sheet.streamlit.app/) |
| Streamlit Chat API Docs | [https://docs.streamlit.io/develop/api-reference/chat](https://docs.streamlit.io/develop/api-reference/chat) |
| Groq Console | [https://console.groq.com/](https://console.groq.com/) |
