from datetime import date, timedelta
from app.tools.db_tools import meeting_exists, create_meeting
from app.agents.weather_agent import handle as weather_handle
import re

def extract_city(query: str):
    match = re.search(r"in\s+([a-zA-Z]+)", query.lower())
    if match:
        return match.group(1).capitalize()
    return None

def is_weather_good(weather_text: str) -> bool:
    bad_keywords = ["rain", "storm", "snow", "thunder"]
    weather_text = weather_text.lower()

    return not any(word in weather_text for word in bad_keywords)


def handle(query: str):
    query_lower = query.lower()

    if "tomorrow" in query_lower:
        meeting_date = date.today() + timedelta(days=1)
    else:
        meeting_date = date.today()

 
    weather_result = weather_handle(
        f"what is the weather tomorrow?"
        if "tomorrow" in query_lower
        else "what is the weather today?"
    )

    if not is_weather_good(weather_result):
        return f"Meeting not scheduled because weather is not good.\n{weather_result}"

    existing = meeting_exists(meeting_date)
    if existing:
        return f"Meeting already scheduled on {meeting_date}"

    meeting = create_meeting("Team Meeting", meeting_date)

    return f"Meeting scheduled successfully on {meeting.date}"
