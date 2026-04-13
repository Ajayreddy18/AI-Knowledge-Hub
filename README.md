# AI Knowledge Hub – Multimodal AI Assistant

AI Knowledge Hub is a **multimodal Retrieval-Augmented Generation (RAG) system** that allows users to query **documents, images, audio, and video files using natural language**.

It is designed as a **0→1 AI product MVP** for startup use cases such as enterprise knowledge assistants, internal copilots, multimodal search, and workflow automation.

The system processes uploaded content, converts it into embeddings, stores it in a **FAISS vector database**, and uses an **LLM-powered retrieval workflow** to generate context-grounded answers.

---

# 🚀 Real-World Use Cases

This project is built to demonstrate practical AI product workflows that early-stage startups can ship fast.

### Best-fit use cases

* **Enterprise knowledge assistants** for PDFs, reports, and SOPs
* **Internal team copilots** for searching mixed media content
* **Customer support knowledge retrieval systems**
* **Research workflow acceleration** across documents and transcripts
* **Multimodal learning assistants** for educational content
* **AI-powered document and media search platforms**

---

# ✨ Core Features

## 📄 Document Processing

* Upload **PDF, DOCX, TXT** files
* Automatic text extraction and chunking
* Stores embeddings for semantic retrieval
* Enables question answering over uploaded files

## 🖼️ Image Processing

* OCR-based text extraction using **Tesseract**
* Supports scanned images and screenshots
* Converts images into searchable text

## 🎙️ Audio Processing

* Converts speech → text using **Whisper**
* Supports multiple audio formats
* Enables voice-driven knowledge workflows

## 🎥 Video Processing

* Extracts audio using **FFmpeg**
* Converts speech → text
* Extracts key frames using **OpenCV**
* Generates contextual summaries from video content

## 🤖 AI Chat (RAG Workflow)

* Uses **FAISS vector database**
* Retrieves contextually relevant chunks
* Generates grounded responses with **TinyLlama**
* Natural-language chat over multimodal content

## 🧠 Smart Analyzer

* Automatically detects uploaded file type
* Routes content through the correct processing pipeline
* Simplifies product integration workflows

---

# 🏗️ System Workflow

```text
User Upload
   ↓
File Type Detection
   ↓
Text / OCR / Speech Extraction
   ↓
Chunking + Embedding Generation
   ↓
FAISS Vector Storage
   ↓
Semantic Retrieval
   ↓
TinyLlama Response Generation
   ↓
Final Context-Aware Answer
```

This architecture demonstrates a **production-style AI backend workflow** from ingestion to answer generation.

---

# 🛠️ Tech Stack

| Component        | Technology               |
| ---------------- | ------------------------ |
| Backend API      | FastAPI                  |
| LLM              | TinyLlama (Transformers) |
| Speech-to-Text   | Whisper                  |
| Vector Database  | FAISS                    |
| OCR              | Tesseract                |
| Video Processing | OpenCV + FFmpeg          |
| Frontend         | HTML                     |
| Local Inference  | Ollama-ready workflows   |

---

# 📂 Project Structure

```text
AI-Knowledge-Hub/
│
├── backend/
│   ├── app.py                  # Main FastAPI app
│   ├── llm.py                  # LLM response generation
│   ├── vector_store.py         # FAISS indexing & semantic search
│   ├── document_loader.py      # Document + OCR processing
│   ├── speech_to_text.py       # Audio transcription
│   ├── video_processor.py      # Video frame extraction
│   ├── video_audio.py          # Audio extraction from video
│
├── frontend/
│   └── index.html              # Lightweight UI
│
├── data/                       # Stored processed files
├── temp/                       # Temporary generated assets
├── requirements.txt
└── README.md
```

The modular structure is intentionally designed to reflect **clean separation of concerns for backend AI systems**.

---

# ⚙️ Installation Guide

## 1) Clone Repository

```bash
git clone https://github.com/Ajayreddy18/AI-Knowledge-Hub.git
cd AI-Knowledge-Hub
```

## 2) Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

## 3) Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 4) Install System Dependencies

Make sure these are installed:

* **FFmpeg** → audio/video extraction
* **Tesseract OCR** → image text extraction

---

# ▶️ Run the Backend Server

```bash
uvicorn backend.app:app --reload
```

### Open Swagger API Docs

```text
http://127.0.0.1:8000/docs
```

---

# 🔌 API Endpoints

## Upload File

```text
POST /upload/
```

Supports:

* PDF
* DOCX
* TXT
* images

## Chat Query

```text
POST /chat/
```

Input:

```json
{
  "query": "Summarize the uploaded PDF"
}
```

## Audio Input

```text
POST /audio/
```

Upload an audio file for speech-to-text + retrieval.

## Video Input

```text
POST /video/
```

Upload video for transcript + frame analysis.

## Smart Analyzer

```text
POST /analyze/
```

Auto-detects the file type and routes processing.

---

# 📬 Example API Usage

```bash
curl -X POST "http://127.0.0.1:8000/chat/" \
-H "Content-Type: application/json" \
-d '{"query":"Give me a summary of the uploaded video"}'
```

---

# 🧩 How It Works Internally

1. User uploads a file
2. System extracts content (OCR / STT / parsing)
3. Text is chunked and converted into embeddings
4. Embeddings are stored in **FAISS**
5. User sends a natural-language query
6. Relevant chunks are retrieved semantically
7. **TinyLlama** generates the final answer

This reflects a **backend-first AI product architecture** suitable for MVPs and startup demos.

---

# 📈 Future Improvements / Roadmap

* Async background jobs with **Celery + Redis**
* **Dockerized deployment** for cloud environments
* **AWS S3** for file storage
* **PostgreSQL metadata layer**
* Streaming responses with **WebSockets**
* Multi-user auth + workspace isolation
* Agentic workflow routing
* Better multimodal frame reasoning

---

# 📌 Important Notes

* Avoid uploading files larger than **100MB**
* `venv/` is excluded using `.gitignore`
* Temporary files are auto-generated
* Designed as an **MVP-ready AI backend system** for fast experimentation

---

# 💡 Why This Project Matters

This project showcases my ability to independently build:

* multimodal ingestion pipelines
* retrieval systems
* vector search workflows
* FastAPI backend APIs
* local LLM inference
* product-ready AI MVPs

It represents the type of **0→1 AI backend product engineering** I enjoy building for fast-moving startups

