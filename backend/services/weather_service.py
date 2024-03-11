import requests
from config import settings


def fetch_weather_data_by_coordinates(latitude, longitude):
    api_key = settings.OPENWEATHERMAP_API_KEY
    # one unit of 'cnt' equals to 3 hours
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}&units=metric&cnt=8'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
