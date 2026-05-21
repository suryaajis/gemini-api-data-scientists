# LLM-Based Tools & Gemini API Integration for Data Scientists

**Program: Maju Bareng AI** — Organized by [Hacktiv8](https://www.hacktiv8.com)
Supported by Google.org and the Asian Development Bank.

---

## About This Program

This repository contains all materials, notebooks, and scripts for the **Maju Bareng AI** training program — a 1-week intensive course designed to equip data scientists with practical LLM integration skills using the Gemini API, LangChain, and Streamlit.

| | |
|---|---|
| **Total Sessions** | 3 |
| **Total Duration** | 10 Hours |
| **Platform** | Online — Google Classroom & Google Meet |
| **Prerequisites** | Python, Machine Learning, NLP basics |

---

## Project Structure

```
gemini-api-data-scientists/
├── session-1/              # Intro to AI & Gemini Implementation
│   ├── gemini_api.py       # Full Python script
│   ├── gemini_api.ipynb    # Jupyter Notebook (cell-by-cell)
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # API key template
│   └── docs/               # Session notes & summaries
├── session-2/              # RAG with LangChain
├── session-3/              # Chatbot with LLM + Streamlit
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
- Advanced Prompting Techniques (CoT, ToT, ReAct)
- Google Gemini Configuration (temperature, top-k, top-p, max tokens)
- Function Calling

**Hands-On:**
- Generate text from text, image, audio, and PDF inputs using Gemini API
- Configure Gemini generation parameters

**Quick Start:**
```bash
# 1. Create virtual environment
conda create -n gemini-api python=3.11 -y
conda activate gemini-api

# 2. Install dependencies
pip install -r session-1/requirements.txt

# 3. Set up API key
cp session-1/.env.example session-1/.env
# Edit .env and fill in: GEMINI_API_KEY=your_key_here

# 4. Run
python session-1/gemini_api.py
# or open session-1/gemini_api.ipynb in VS Code
```

Get your Gemini API key at: https://aistudio.google.com/

---

## Session 2 — RAG with LangChain

**Topics Covered:**
- Introduction to RAG (Retrieval-Augmented Generation)
- Vector Database concepts and usage
- Introduction to LangChain framework

**What is RAG?**
RAG is a technique that combines a retrieval system with a language model. Instead of relying solely on the model's training data, RAG retrieves relevant documents from an external knowledge base and passes them as context to the LLM — reducing hallucinations and enabling up-to-date answers.

```
User Query → Retriever → Relevant Documents
                                ↓
                   LLM + Context → Answer
```

**Hands-On:**
- Build a RAG pipeline using LangChain
- Set up and query a Vector Database
- Connect Gemini API with LangChain

> Materials coming after Session 1 completion.

---

## Session 3 — Building a Chatbot with LLM + Streamlit

**Topics Covered:**
- Building an LLM-powered Chatbot with Streamlit
- Deploying Streamlit apps to the Cloud

**What We Build:**
A fully functional chatbot web app powered by Gemini API, built with Streamlit and deployed to the cloud — accessible via browser without any local setup.

```
User (Browser) → Streamlit App → Gemini API → Response
```

**Hands-On:**
- Build a ChatGPT-style chatbot UI with Streamlit
- Integrate conversation history and context
- Deploy the app to Streamlit Cloud

> Materials coming after Session 2 completion.

---

## Setup Guide

### 1. Prerequisites
- Python 3.11+
- Miniconda (recommended) or any Python virtual environment
- VS Code with **Python** and **Jupyter** extensions
- A Google account to get a Gemini API key

### 2. Get Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Click **Get API Key** → **Create API Key**
3. Copy the key

### 3. Environment Setup
```bash
# Using Miniconda (recommended)
conda create -n gemini-api python=3.11 -y
conda activate gemini-api

# Install for specific session
pip install -r session-1/requirements.txt
```

### 4. API Key Configuration
Each session folder has a `.env.example` file. Copy and fill it:
```bash
cp session-1/.env.example session-1/.env
```
Then edit `.env`:
```
GEMINI_API_KEY=your_api_key_here
```

> **Never commit your `.env` file** — it's already in `.gitignore`.

---

## Program Checklist

| Phase | Task | Due |
|---|---|---|
| Session 1 | Pre-Test + Attendance + Quiz 1 | Session 1 day |
| Session 2 | Attendance + Quiz 2 | Session 2 day |
| Session 3 | Attendance + Quiz 3 + Post-Test | Session 3 day |
| Final Project | Form Submission | H+2 after Session 3 |

### Certificate Requirements

| Tier | Attendance | Survey | Quiz | Final Project |
|---|---|---|---|---|
| **Tier 1** | 2/3 | 2/2 | 3/3 | Required |
| **Tier 2** | 2/3 | 2/2 | 3/3 | Not required |

---

## References

- [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [LangChain Docs](https://python.langchain.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Prompting Guide](https://www.promptingguide.ai/techniques)
- [Google AI Safety](https://ai.google/safety/)
