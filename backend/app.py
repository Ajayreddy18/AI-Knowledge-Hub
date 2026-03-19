from fastapi import FastAPI, UploadFile, File, Form
import os
from document_loader import load_document
from vector_store import add_to_index, search
from llm import generate_answer
from speech_to_text import transcribe_audio
from video_processor import extract_frames
from video_audio import extract_audio_text

app = FastAPI()

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs("temp", exist_ok=True)


@app.get("/")
def root():
    return {"message": "AI Knowledge Hub is running!"}


# 🔥 UPLOAD API
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join("temp", file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = load_document(file_path)

    print("===== OCR TEXT FROM API =====")
    print(text)
    print("=============================")

    if not text or text.strip() == "":
        return {"message": "No text extracted"}

    add_to_index(text)

    return {
        "filename": file.filename,
        "message": "File processed and added to knowledge base"
    }


# 🔥 CHAT API
@app.post("/chat/")
async def chat(query: str = Form(...)):

    print("USER QUERY:", query)

    results = search(query)

    print("SEARCH RESULTS:", results)

    if not results:
        return {"query": query, "answer": "No relevant data found"}

    context = " ".join(results)

    answer = generate_answer(context, query)

    if not answer:
        answer = "Answer could not be generated"

    return {
        "query": query,
        "answer": answer
    }


# 🔥 AUDIO API
@app.post("/audio/")
async def audio_chat(file: UploadFile = File(...)):

    file_path = os.path.join("temp", file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Speech → Text
    query = transcribe_audio(file_path)

    if not query:
        return {"error": "Could not understand audio"}

    print("USER AUDIO QUERY:", query)

    results = search(query)

    if not results:
        return {"query": query, "answer": "No relevant data found"}

    context = " ".join(results)

    answer = generate_answer(context, query)

    return {
        "query": query,
        "answer": answer
    }


# 🔥 VIDEO API (FIXED)
@app.post("/video/")
async def video_chat(file: UploadFile = File(...)):

    video_path = os.path.join("temp", file.filename)

    with open(video_path, "wb") as f:
        f.write(await file.read())

    # 1. Speech extraction
    transcript = extract_audio_text(video_path)

    if not transcript:
        return {"error": "No speech detected in video"}

    # 2. Frame extraction
    frames = extract_frames(video_path)

    print("TRANSCRIPT:", transcript)

    # 3. Search (RAG)
    results = search(transcript)

    if not results:
        context = transcript
    else:
        context = " ".join(results)

    # 4. Generate answer (FIXED HERE ✅)
    answer = generate_answer(context, transcript)

    return {
        "status": "success",
        "transcript": transcript,
        "frames_extracted": len(frames),
        "summary": answer,
        "message": "Video processed successfully using multimodal AI pipeline"
    }


# 🔥 UNIVERSAL ANALYZE API (FIXED)
@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):

    filename = file.filename.lower()
    path = os.path.join("temp", filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    # 🎥 VIDEO CASE
    if filename.endswith(".mp4"):

        transcript = extract_audio_text(path)
        frames = extract_frames(path)

        results = search(transcript)

        context = " ".join(results) if results else transcript

        answer = generate_answer(context, transcript)

        return {
            "type": "video",
            "transcript": transcript,
            "frames": len(frames),
            "answer": answer
        }

    # 🎤 AUDIO CASE
    else:
        query = transcribe_audio(path)

        results = search(query)

        context = " ".join(results) if results else query

        answer = generate_answer(context, query)

        return {
            "type": "audio",
            "query": query,
            "answer": answer
        }