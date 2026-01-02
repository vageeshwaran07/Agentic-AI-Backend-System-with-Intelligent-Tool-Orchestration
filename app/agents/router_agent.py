def router(query: str):
    q = query.lower()

    if "schedule" in q or "meeting" in q and "verify" in q:
        return "meeting"

    if "weather" in q:
        return "weather"

    if "policy" in q or "document" in q:
        return "document"

    if "meeting" in q:
        return "db"

    return "unknown"
