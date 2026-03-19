import whisper


model = whisper.load_model("base")  # you can use "tiny", "base", "small"

def transcribe_audio(file_path):
    try:
        result = model.transcribe(file_path)
        text = result["text"]

        print("===== AUDIO TEXT =====")
        print(text)
        print("======================")

        return text

    except Exception as e:
        print("ERROR in speech:", e)
        return None