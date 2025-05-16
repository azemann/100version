from PIL import Image
import pytesseract

def extract_image_text(path):
    return pytesseract.image_to_string(Image.open(path), lang="fra")
