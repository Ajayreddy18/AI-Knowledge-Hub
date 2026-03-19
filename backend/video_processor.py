import cv2
import os

def extract_frames(video_path, output_dir="frames", interval_sec=2):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval_sec)

    frames = []
    count = 0
    saved = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % frame_interval == 0:
            path = f"{output_dir}/frame_{saved}.jpg"
            cv2.imwrite(path, frame)
            frames.append(path)
            saved += 1

        count += 1

    cap.release()
    return frames