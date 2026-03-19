import os
from pypdf import PdfReader
import docx
import cv2
import pytesseract
from PIL import Image
import pytesseract

# Set path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract\tesseract.exe"

def load_image(file_path):
    try:
        # Read image using OpenCV
        img = cv2.imread(file_path)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Improve OCR accuracy
        gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

        # Extract text
        text = pytesseract.image_to_string(gray)

        print("===== OCR TEXT FROM API =====")
        print(text)
        print("=============================")

        if not text.strip():
            return "No readable text found in image."

        return text

    except Exception as e:
        print("OCR ERROR:", str(e))
        return "Error extracting text from image."

def load_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text
    print("OCR TEXT:", text)
def load_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
def load_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return load_pdf(file_path)
    elif ext == ".docx":
        return load_docx(file_path)
    elif ext == ".txt":
        return load_txt(file_path)
    elif ext in [".png", ".jpg", ".jpeg"]:
        return load_image(file_path)
    else:
        return "Unsupported file format"