# LLM-Based Tools & Gemini API Integration for Data Scientists

**Program: Maju Bareng AI** — Organized by [Hacktiv8](https://www.hacktiv8.com)  
Supported by Google.org, AVPN, and the Asian Development Bank (AI Opportunity Fund: Asia Pacific)

---

## About This Program

This repository contains all materials, notebooks, and scripts for the **Maju Bareng AI** training program — a 3-session intensive course designed to equip data scientists with practical LLM integration skills using the Gemini API, LangChain, Llama, and Streamlit.

| | |
|---|---|
| **Total Sessions** | 3 |
| **Platform** | Online — Google Classroom & Google Meet |
| **Prerequisites** | Python, Machine Learning, NLP basics |
| **Organizer** | PT. Hacktivate Teknologi Indonesia (Hacktiv8) |

---

## Project Structure

```
gemini-api-data-scientists/
├── session-1/                        # Intro to AI & Gemini Implementation
│   ├── gemini_api.py                 # Full Python script
│   ├── gemini_api.ipynb              # Jupyter Notebook
│   ├── requirements.txt              # Python dependencies
│   ├── .env.example                  # API key template
│   └── docs/
│       ├── introduction.md           # Session 1 material summary
│       └── first-preparation.md      # Setup guide
├── session-2/                        # RAG with LangChain & Llama
│   ├── rag_llama_avpn.py             # Full Python script
│   ├── rag_llama_avpn.ipynb          # Jupyter Notebook
│   ├── requirements.txt              # Python dependencies
│   ├── .env.example                  # API key template
│   └── docs/
│       ├── material.md               # Session 2 material summary
│       └── first-preparation.md      # Setup guide
├── session-3/                        # Chatbot with LLM + Streamlit + AI Agents
│   └── docs/
│       ├── sesi-3-summary.md         # Session 3 material summary
│       └── gemini-streamlit-chatbot-summary.md  # Streamlit chatbot reference
├── gemini-streamlit-chatbot-summary.md  # YouTube tutorial summary
├── .gitignore
└── README.md
```

---

## Session 1 — Introduction to AI & Gemini Implementation

**Topics Covered:**
- AI, Generative AI & LLM concepts and ethics
- Introduction to Chatbot (Rule-based vs AI Chatbot)
- Hallucination & Basic Prompting Techniques
- Introduction to Google Gemini & Gemini API
- Text generation from various input types (text, image, audio, PDF)
- Advanced Prompting Techniques (Chain-of-Thought, Tree-of-Thought, ReAct)
- Google Gemini Configuration (temperature, top-k, top-p, max tokens)
- Function Calling

**Hands-On:**
- Generate text from text, image, audio, and PDF inputs using Gemini API
- Configure Gemini generation parameters
- Implement function calling

**Quick Start:**
```bash
# 1. Create virtual environment
conda create -n gemini-api python=3.11 -y
conda activate gemini-api

# 2. Install dependencies
pip install -r session-1/requirements.txt

# 3. Set up API key
cp session-1/.env.example session-1/.env
# Edit .env: GEMINI_API_KEY=your_key_here

# 4. Run
python session-1/gemini_api.py
# or open session-1/gemini_api.ipynb in VS Code / Jupyter
```

Get your Gemini API key at: https://aistudio.google.com/

---

## Session 2 — RAG with LangChain & Llama

**Topics Covered:**
- Introduction to RAG (Retrieval-Augmented Generation)
- Vector Database (Faiss, Chroma, Pinecone, etc.)
- Introduction to LangChain framework & Prompt Templates
- Introduction to Llama (Meta's open-source LLM via Groq Cloud)

**What is RAG?**

RAG is a technique that combines a retrieval system with a language model. Instead of relying solely on the model's training data, RAG retrieves relevant documents from an external knowledge base and passes them as context to the LLM — reducing hallucinations and enabling up-to-date answers.

```
Dokumen PDF/Data
      ↓ (Embedding Model)
Vector Database (Faiss / ChromaDB)
      ↓ (Semantic Search)
Dokumen Relevan
      ↓ (LangChain Chain)
LLM (Gemini / Llama) + Konteks
      ↓
Jawaban Akurat & Relevan
```

**Key Technologies:**

| Teknologi | Peran |
|---|---|
| **LangChain** | Framework untuk membangun pipeline RAG |
| **Faiss** | Vector database untuk menyimpan dan mencari embedding |
| **PyMuPDF** | Membaca dan memproses dokumen PDF |
| **Gemini API** | LLM untuk generating respons |
| **Llama via Groq** | Alternatif LLM open-source gratis |
| **LangGraph** | Orkestrasi agent berbasis graf |

**Hands-On:**
- Build a RAG pipeline using LangChain + Faiss
- Query a PDF document as a knowledge base
- Connect Gemini API and Llama (via Groq) with LangChain

**Quick Start:**
```bash
# 1. Install dependencies
pip install -r session-2/requirements.txt

# 2. Set up API keys
cp session-2/.env.example session-2/.env
# Edit .env:
#   GEMINI_API_KEY=your_gemini_key
#   GROQ_API_KEY=your_groq_key

# 3. Run
python session-2/rag_llama_avpn.py
# or open session-2/rag_llama_avpn.ipynb
```

Get your Groq API key at: https://console.groq.com/

---

## Session 3 — Building a Chatbot with LLM + Streamlit & AI Agents

**Topics Covered:**
- Building an LLM-powered Chatbot with Streamlit
- Streamlit widgets (chat, charts, status)
- Introduction to AI Agents
- AI Agent use cases (Data Agent, Customer Service Agent, Code Agent)
- Deploying Streamlit apps to the Cloud

### Streamlit

**Streamlit** is an open-source Python framework for building interactive web apps — specifically for data science and ML — without writing any HTML, CSS, or JavaScript.

**Key Streamlit Widget Categories:**

| Category | Widgets |
|---|---|
| **Chat** | `st.chat_input`, `st.chat_message`, `st.status` |
| **Charts** | `st.area_chart`, `st.bar_chart`, `st.line_chart` |
| **Status** | `st.progress`, `st.spinner`, `st.status` |

### AI Agents

AI Agents are software programs that can autonomously interact with their environment, collect data, and execute tasks using a set of tools (function calling) to achieve a defined goal.

**AI Agents vs AI Assistants:**

| | AI Agents | AI Assistant |
|---|---|---|
| **Goal** | Autonomously execute tasks using tools | Suggest actions to the user |
| **Capability** | Complex tasks (e.g., analyze last month's expenses) | Information only (e.g., how to check balance) |
| **Interaction** | **Proactive** — goal-oriented | **Reactive** — responds to requests |

**Use Case Examples:**

| Agent Type | Description |
|---|---|
| **Data Agent** | Analyzes data to answer business questions (sales, customers, trends) |
| **Customer Service Agent** | Resolves customer complaints and takes direct action |
| **Code Agent** | Helps developers write cleaner code and fix bugs |

**Hands-On:**
- Build a chatbot UI with Streamlit + LLM integration
- Implement an AI Agent with function calling
- Deploy the Streamlit app to Streamlit Cloud

---

## Setup Guide

### 1. Prerequisites
- Python 3.11+
- Miniconda (recommended) or any Python virtual environment
- VS Code with **Python** and **Jupyter** extensions
- A Google account for Gemini API key
- A Groq account for Llama API key

### 2. Get API Keys

**Gemini API Key:**
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Click **Get API Key** → **Create API Key**

**Groq API Key (for Llama):**
1. Go to [Groq Console](https://console.groq.com/)
2. Navigate to **API Keys** → **Create API Key**

### 3. Environment Setup
```bash
# Create and activate environment
conda create -n gemini-api python=3.11 -y
conda activate gemini-api

# Install for a specific session
pip install -r session-1/requirements.txt  # or session-2/
```

### 4. API Key Configuration
Each session has a `.env.example`. Copy and fill it:
```bash
cp session-1/.env.example session-1/.env
```
Then edit `.env`:
```
GEMINI_API_KEY=your_gemini_key_here
GROQ_API_KEY=your_groq_key_here
```

> **Never commit your `.env` file** — it's already in `.gitignore`.

---

## Program Checklist

| Phase | Task | Due |
|---|---|---|
| Session 1 | Pre-Test + Attendance + Quiz 1 | Session 1 day |
| Session 2 | Attendance + Quiz 2 | Session 2 day |
| Session 3 | Attendance + Quiz 3 + Post-Test | Session 3 day |
| Final Project | GitHub repo + UI screenshots | H+2 after Session 3 |

### Certificate Requirements

| Tier | Attendance | Survey | Quiz | Final Project |
|---|---|---|---|---|
| **Tier 1** | 2/3 | 2/2 | 3/3 | Required |
| **Tier 2** | 2/3 | 2/2 | 3/3 | Not required |

---

## Final Project

Build an AI-powered chatbot with a use case and parameter configuration of your choice. The chatbot must use an NLP/LLM model to process natural language and provide relevant responses.

**Example use cases:** customer service bot, education bot, travel assistant, personal productivity assistant

**Deliverables:**
- GitHub repository URL
- Screenshots of the User Interface

---

## References

- [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [LangChain Docs](https://python.langchain.com/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)
- [Groq Console & Docs](https://console.groq.com/docs/quickstart)
- [Prompting Guide](https://www.promptingguide.ai/techniques)
- [Google AI Safety](https://ai.google/safety/)
