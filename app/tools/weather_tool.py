import requests
from app.config import OPENWEATHER_API_KEY


def get_weather_today(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        return None

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }


def get_weather_tomorrow(city: str):
    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        return None

    tomorrow_data = data["list"][8]

    return {
        "city": city,
        "temperature": tomorrow_data["main"]["temp"],
        "description": tomorrow_data["weather"][0]["description"]
    }
