from app.tools.llm_tools import ask_llm

def fast_rule_router(query: str):
    q = query.lower()

    if "schedule" in q or "meeting" in q:
        return "meeting"

    if "weather" in q:
        return "weather"

    if "policy" in q or "document" in q:
        return "document"

    if "list" in q or "show" in q:
        return "db"

    return None


def route_query(query: str):
 
    decision = fast_rule_router(query)
    if decision:
        return decision

    prompt = f"""
Choose the correct handler:
weather | document | meeting | db

User query:
{query}
"""

    result = ask_llm(prompt).lower()

    for k in ["weather", "document", "meeting", "db"]:
        if k in result:
            return k

    return "unknown"
