from app.tools.web_search import web_search

DOCUMENT_LINES = []


def set_document(lines: list[str]):
    global DOCUMENT_LINES
    DOCUMENT_LINES = lines


def handle(query: str):
    if not DOCUMENT_LINES:
        return "No document uploaded yet."

    query_words = set(query.lower().split())

    matched_lines = []

    for line in DOCUMENT_LINES:
        line_words = set(line.lower().split())

  
        if query_words & line_words:
            matched_lines.append(line)

    if matched_lines:
        return " ".join(matched_lines[:5])


    return web_search(query)
