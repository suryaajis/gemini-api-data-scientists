# LLM-Based Tools & Gemini API Integration for Data Scientists

**Program: Maju Bareng AI** — Organized by [Hacktiv8](https://www.hacktiv8.com)  
Supported by Google.org, AVPN, and the Asian Development Bank (AI Opportunity Fund: Asia Pacific)

---

## About This Program

This repository contains all materials, notebooks, and scripts for the **Maju Bareng AI** training program — a 3-session intensive course designed to equip data scientists with practical LLM integration skills using the Gemini API, LangChain, Llama, and Streamlit. The program culminates in a **Final Project** where participants build a full AI-powered chatbot application.

| | |
|---|---|
| **Total Sessions** | 3 + Final Project |
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
│   ├── requirements.txt
│   ├── .env.example
│   └── docs/
│       ├── introduction.md
│       └── first-preparation.md
├── session-2/                        # RAG with LangChain & Llama
│   ├── rag_llama_avpn.py             # Full Python script
│   ├── rag_llama_avpn.ipynb          # Jupyter Notebook
│   ├── requirements.txt
│   ├── .env.example
│   └── docs/
│       ├── material.md
│       └── first-preparation.md
├── session-3/                        # Chatbot with Streamlit + AI Agents
│   ├── streamlit-chatbot/
│   │   ├── app.py                    # Streamlit chatbot app
│   │   ├── streamlit_chatbot.ipynb
│   │   └── requirements.txt
│   ├── ai-agents/
│   │   ├── ai_agents.py              # SQL Agent + BaristaBot CLI
│   │   ├── ai_agents.ipynb
│   │   ├── requirements.txt
│   │   └── .env.example
│   └── docs/
│       ├── sesi-3-summary.md
│       └── gemini-streamlit-chatbot-summary.md
├── final-project/                    # LittleSteps AI — Baby Development Chatbot
│   ├── app.py                        # Main Streamlit application
│   ├── run_ngrok.py                  # ngrok tunnel helper for public URL
│   ├── littlesteps_ai_streamlit.ipynb
│   ├── requirements.txt
│   └── .env.example
├── .gitignore
├── CLAUDE.md
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

### Streamlit Chatbot

**Streamlit** is an open-source Python framework for building interactive web apps — specifically for data science and ML — without writing any HTML, CSS, or JavaScript.

**Key Streamlit Widget Categories:**

| Category | Widgets |
|---|---|
| **Chat** | `st.chat_input`, `st.chat_message`, `st.status` |
| **Charts** | `st.area_chart`, `st.bar_chart`, `st.line_chart` |
| **Status** | `st.progress`, `st.spinner`, `st.status` |

**Quick Start:**
```bash
pip install -r session-3/streamlit-chatbot/requirements.txt
streamlit run session-3/streamlit-chatbot/app.py
```

### AI Agents

AI Agents are software programs that can autonomously interact with their environment, collect data, and execute tasks using a set of tools (function calling) to achieve a defined goal.

**AI Agents vs AI Assistants:**

| | AI Agents | AI Assistant |
|---|---|---|
| **Goal** | Autonomously execute tasks using tools | Suggest actions to the user |
| **Capability** | Complex tasks (e.g., analyze last month's expenses) | Information only (e.g., how to check balance) |
| **Interaction** | **Proactive** — goal-oriented | **Reactive** — responds to requests |

The `session-3/ai-agents/ai_agents.py` script demonstrates two agents built with LangGraph:
- **SQL Agent** — answers natural-language questions about a SQLite database
- **BaristaBot** — a stateful coffee-ordering CLI bot with conversation memory (`InMemorySaver`)

**Quick Start (AI Agents):**
```bash
pip install -r session-3/ai-agents/requirements.txt
cp session-3/ai-agents/.env.example session-3/ai-agents/.env
# Edit .env: GEMINI_API_KEY=your_key_here
python session-3/ai-agents/ai_agents.py
# Type 'q' to quit BaristaBot
```

---

## Final Project — LittleSteps AI

**LittleSteps AI** is a baby growth and development assistant chatbot built as the capstone project for the Maju Bareng AI program. It helps parents track developmental milestones and get evidence-based parenting guidance powered by Gemini AI.

### Features

- **Baby Profile Setup** — enter name, age (months), gender, weight, and height in the sidebar
- **Milestone Tracker** — built-in milestone reference data covering 0–36 months across motor, cognitive, and social-emotional domains
- **Conversational AI** — Gemini 2.5 Flash chat session with a personalized system prompt tailored to each baby's profile
- **Quick Prompts** — one-click preset questions for common parenting topics (MPASI, sleep tips, brain stimulation, etc.)
- **Medical Disclaimer** — always reminds users to consult a pediatrician for health concerns
- **ngrok Integration** — `run_ngrok.py` exposes the local Streamlit app via a public tunnel for sharing/demo

### Tech Stack

| Component | Technology |
|---|---|
| **UI Framework** | Streamlit |
| **LLM** | Gemini 2.5 Flash (`google-genai` SDK) |
| **Tunnel** | pyngrok |
| **Config** | python-dotenv |

### Architecture

```
Sidebar (Baby Profile)
      ↓ save profile
LittleStepsBot (google.genai.Client)
      ↓ personalized system_instruction
Gemini 2.5 Flash Chat Session
      ↓
Chat UI (st.chat_message) + Milestone Expander
```

The `LittleStepsBot` class wraps `genai.Client` and `client.chats.create()`. A new chat session is created (or reset) whenever the baby profile is updated, ensuring the system prompt always reflects the latest profile data.

### Quick Start

```bash
# 1. Install dependencies
pip install -r final-project/requirements.txt

# 2. Set up API key
cp final-project/.env.example final-project/.env
# Edit .env: GEMINI_API_KEY=your_key_here

# 3. Run locally
streamlit run final-project/app.py

# 4. (Optional) Expose via ngrok for public access
python final-project/run_ngrok.py
```

---

## Setup Guide

### 1. Prerequisites
- Python 3.11+
- Miniconda (recommended) or any Python virtual environment
- VS Code with **Python** and **Jupyter** extensions
- A Google account for Gemini API key
- A Groq account for Llama API key (Session 2 only)

### 2. Get API Keys

**Gemini API Key:**
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Click **Get API Key** → **Create API Key**

**Groq API Key (for Llama — Session 2 only):**
1. Go to [Groq Console](https://console.groq.com/)
2. Navigate to **API Keys** → **Create API Key**

### 3. Environment Setup
```bash
# Create and activate environment
conda create -n gemini-api python=3.11 -y
conda activate gemini-api

# Install for a specific session
pip install -r session-1/requirements.txt   # session 1
pip install -r session-2/requirements.txt   # session 2
pip install -r session-3/streamlit-chatbot/requirements.txt  # session 3 chatbot
pip install -r session-3/ai-agents/requirements.txt          # session 3 agents
pip install -r final-project/requirements.txt                # final project
```

### 4. API Key Configuration

Each session and the final project have a `.env.example`. Copy and fill it:
```bash
cp session-1/.env.example session-1/.env
cp final-project/.env.example final-project/.env
```
Then edit the `.env` file:
```
GEMINI_API_KEY=your_gemini_key_here
GROQ_API_KEY=your_groq_key_here   # session 2 only
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

## References

- [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [LangChain Docs](https://python.langchain.com/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)
- [Groq Console & Docs](https://console.groq.com/docs/quickstart)
- [Prompting Guide](https://www.promptingguide.ai/techniques)
- [Google AI Safety](https://ai.google/safety/)
