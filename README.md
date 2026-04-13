AI Knowledge Hub – Multimodal AI Assistant

AI Knowledge Hub is a powerful Multimodal AI Assistant that can process and understand multiple types of data including:

-  Documents (PDF, TXT, DOCX)
- Images (OCR text extraction)
- Audio (Speech-to-Text)
- Video (Audio + Frame Processing)

The system uses Retrieval-Augmented Generation (RAG) to provide intelligent, context-based answers.

Project Overview

This project allows users to upload different types of files and interact with them using AI.

 It extracts content from files  
 Stores it in a vector database  
 Allows users to ask questions  
 Generates accurate answers using an LLM  

Features

Document Processing
- Upload PDF, DOCX, TXT files
- Extracts and stores text
- Enables question-answering

Image Processing
- Extracts text using OCR
- Supports scanned images
- Converts images → readable text

Audio Processing
- Converts speech → text using Whisper
- Works with multiple audio formats
- Allows voice-based queries

Video Processing
- Extracts audio from video using FFmpeg
- Converts speech → text
- Extracts frames using OpenCV
- Generates summary of video

AI Chat (RAG System)
- Uses FAISS vector database
- Retrieves relevant context
- Generates answers using LLM

Tech Stack

| Component      | Technology Used |
|----------------|----------------|
| Backend        | FastAPI        |
| LLM            | TinyLlama (Transformers) |
| Speech-to-Text | Whisper        |
| Vector DB      | FAISS          |
| OCR            | Tesseract      |
| Video Handling | OpenCV + FFmpeg |
| Frontend       | HTML           |

Project Structure

```
AI-Knowledge-Hub/
│
├── backend/
│ ├── app.py # Main FastAPI app
│ ├── llm.py # LLM response generation
│ ├── vector_store.py # FAISS indexing & search
│ ├── document_loader.py # Document + OCR processing
│ ├── speech_to_text.py # Audio transcription
│ ├── video_processor.py # Frame extraction
│ ├── video_audio.py # Audio extraction from video
│
├── frontend/
│ └── index.html # Basic UI
│
├── data/ # Stored documents
├── temp/ # Temporary files
├── requirements.txt
└── README.md
```

Installation Guide

 1. Clone Repository


git clone https://github.com/Ajayreddy18/AI-Knowledge-Hub.git

cd AI-Knowledge-Hub

 2. Create Virtual Environment


python -m venv venv
venv\Scripts\activate


 3. Install Dependencies


pip install -r requirements.txt


 4. Install System Dependencies

Make sure you install:

- FFmpeg (for audio/video)
- Tesseract OCR

---

 5. Run Backend Server


uvicorn backend.app:app --reload


 6. Open API Docs


http://127.0.0.1:8000/docs



API Usage

Upload File
- Endpoint: `/upload/`
- Supports: PDF, image, text

Chat
- Endpoint: `/chat/`
- Input: text query

Audio Input
- Endpoint: `/audio/`
- Input: audio file

Video Input
- Endpoint: `/video/`
- Input: video file

Smart Analyzer
- Endpoint: `/analyze/`
- Automatically detects file type

How It Works

1. User uploads file
2. System extracts text (OCR / STT / parsing)
3. Text is converted into embeddings
4. Stored in FAISS vector database
5. User asks a query
6. Relevant data is retrieved
7. LLM generates final answer



 Important Notes

- Do NOT upload large files (>100MB)
- `venv/` is excluded using `.gitignore`
- Temporary files are auto-generated

