from pypdf import PdfReader


def load_pdf_text(file_path: str) -> list[str]:
    reader = PdfReader(file_path)

    text_blocks = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            text_blocks.extend(lines)

    return text_blocks
