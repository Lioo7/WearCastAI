import requests
from config import settings

OPENWEATHERMAP_API_KEY = settings.OPENWEATHERMAP_API_KEY


def fetch_weather_data_by_coordinates(latitude, longitude, units='metric', cnt=6):
    # one unit of 'cnt' equals to 3 hours
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={OPENWEATHERMAP_API_KEY}&units={units}&cnt={cnt}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def fetch_weather_data_by_city(city, units='metric', cnt=6):
    # one unit of 'cnt' equals to 3 hours
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHERMAP_API_KEY}&units={units}&cnt={cnt}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
