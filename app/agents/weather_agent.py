import re
from app.tools.weather_tool import get_weather_today, get_weather_tomorrow


def extract_city(query: str):
    query = query.lower().strip()
    query = re.sub(r"[^a-z\s]", "", query)

    match = re.search(r"in\s+([a-z]+)", query)
    if match:
        return match.group(1).capitalize()

    return None


def handle(query: str):
    city = extract_city(query)

    if not city:
        return "Please ask like: 'What is the weather in Chennai?'"
    
    if "yesterday" in query.lower():
        return (
            " Historical weather requires a paid API plan. "
            "Currently supported: today and tomorrow."
        )

    if "tomorrow" in query.lower():
        data = get_weather_tomorrow(city)
        day = "tomorrow"
    else:
        data = get_weather_today(city)
        day = "today"

    if not data:
        return f"Couldn't fetch weather for {city}"

    return (
        f" Weather in {data['city']} {day}:\n"
        f"Temperature: {data['temperature']}°C\n"
        f"Condition: {data['description']}"
    )
