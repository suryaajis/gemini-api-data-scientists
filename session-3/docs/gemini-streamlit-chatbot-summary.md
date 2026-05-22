# Summary: Build Your Own Chatbot with Gemini 2.0 & Streamlit

**Source:** [YouTube — Build your own Chatbot with Gemini 2.0 & Streamlit! Use text, image, audio or video as input!](https://www.youtube.com/watch?v=We5jYzwXVH8)

---

## Overview

This tutorial walks through building a **multimodal conversational chatbot** using **Google's Gemini 2.0 Flash** model and **Streamlit** as the web interface. The chatbot accepts not just text, but also images, audio files, and video as input — demonstrating the full multimodal power of the Gemini 2.0 API.

---

## Key Technologies

| Tool / Library | Role |
|---|---|
| **Google Gemini 2.0 Flash** | Core LLM powering multimodal understanding |
| **Streamlit** | Web UI framework for the chatbot interface |
| **Google Generative AI SDK** (`google-genai`) | Python client to interact with Gemini API |
| **Google AI Studio** | Platform to generate and manage API keys |

---

## Features Covered

### 1. Text Input
- Standard conversational chat with Gemini 2.0 Flash
- Streaming responses for a real-time chat feel using `generate_content_stream()`

### 2. Image Understanding
- Upload images directly into the chat
- Gemini analyzes the image and answers questions about its content
- Images processed via PIL library

### 3. Audio Processing
- Upload audio files as input
- Gemini processes audio natively without converting to text first
- Enables voice-based Q&A and transcription

### 4. Video Input
- Upload video files for multimodal analysis
- Gemini can reason about visual and audio content within the video

---

## How It Works — Architecture

```
User Input (text / image / audio / video)
        ↓
   Streamlit UI (frontend)
        ↓
   Google Generative AI SDK
        ↓
   Gemini 2.0 Flash API
        ↓
   Streamed Response → Streamlit Chat Interface
```

- Chat history is maintained across turns for a conversational experience
- The app handles different MIME types for each modality

---

## Setup Steps

1. **Get API Key** — Sign into [Google AI Studio](https://aistudio.google.com/) and generate a Gemini API key
2. **Set environment variable:**
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```
3. **Install dependencies:**
   ```bash
   pip install google-genai streamlit
   ```
4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## Key Takeaways

- **Gemini 2.0 Flash** is highly capable for multimodal tasks and is accessible via a free API tier
- **Streamlit** makes it easy to build interactive AI demos without frontend expertise
- A single unified API call handles text, image, audio, and video — no separate pipelines needed
- Streaming responses significantly improve the UX of chatbot interfaces
- The same architecture can be extended with RAG, memory, or tool use

---

## Relevant Links

- [YouTube Tutorial](https://www.youtube.com/watch?v=We5jYzwXVH8)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Docs](https://ai.google.dev/docs)
- [Streamlit Docs](https://docs.streamlit.io/)
