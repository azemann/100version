import fitz, docx
import pytesseract
from PIL import Image

def load_text_file(path):
    if path.endswith(".pdf"):
        text = "\n".join(p.get_text() for p in fitz.open(path))
        if len(text.strip()) < 50:
            return ocr_pdf(path)
        return text
    elif path.endswith(".docx"):
        return "\n".join(p.text for p in docx.Document(path).paragraphs)
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

def ocr_pdf(path):
    doc = fitz.open(path)
    full_text = []
    for page in doc:
        pix = page.get_pixmap(dpi=300)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text = pytesseract.image_to_string(img, lang="fra")
        full_text.append(text)
    return "\n".join(full_text)
