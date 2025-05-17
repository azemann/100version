import fitz, docx

def load_text_file(path):
    if path.endswith(".pdf"):
        return "\n".join(p.get_text() for p in fitz.open(path))
    elif path.endswith(".docx"):
        return "\n".join(p.text for p in docx.Document(path).paragraphs)
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
