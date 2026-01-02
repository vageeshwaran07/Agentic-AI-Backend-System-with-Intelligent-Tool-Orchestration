from datetime import date, timedelta
from app.tools.db_query_tool import get_meetings_for_date, get_meetings_between, get_all_meetings



def handle(query: str):
    q = query.lower()

    today = date.today()
    tomorrow = today + timedelta(days=1)

    if "today" in q:
        meetings = get_meetings_for_date(today)

    elif "tomorrow" in q:
        meetings = get_meetings_for_date(tomorrow)

    elif "next week" in q:
        end = today + timedelta(days=7)
        meetings = get_meetings_between(today, end)

    elif "meeting" in q:
        meetings = get_all_meetings()

    else:
        return "I couldn't understand the database query."

    if not meetings:
        return "No meetings found."

    response_lines = []
    for m in meetings:
        response_lines.append(f"- {m.title} on {m.date}")

    return "\n".join(response_lines)
