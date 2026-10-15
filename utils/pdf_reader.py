from pypdf import PdfReader

def extract_text(file_path):
    """Extract selectable text from a PDF resume."""
    reader = PdfReader(file_path)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages).strip()
