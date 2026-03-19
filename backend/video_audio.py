import whisper
import subprocess
import os

model = whisper.load_model("base")

def extract_audio_text(video_path):
    audio_path = "temp_audio.wav"

    # Extract audio using ffmpeg
    command = f'ffmpeg -y -i "{video_path}" -ar 16000 -ac 1 -c:a pcm_s16le {audio_path}'
    os.system(command)

    result = model.transcribe(audio_path)
    return result["text"]