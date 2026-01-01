def router(query: str):
    query = query.lower()

    if "weather" in query:
        return "weather"

    if "meeting" in query:
        return "meeting"

    if "document" in query or "policy" in query:
        return "document"

    return "unknown"
