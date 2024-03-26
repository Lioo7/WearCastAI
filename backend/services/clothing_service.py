import json
from flask import current_app

from .chat_gpt_service import process_interaction

# Constant for system message
SYSTEM_MESSAGE = (
    """
You are developing a mobile application tailored to provide users with daily clothing recommendations based on the weather forecast in their location. The application receives two crucial inputs: the weather forecast for the next 12 hours and the user's personal preferences, such as cold resistance, style, and gender.

Your task is to generate a concise message that covers the following aspects:

1. **Summary of the Forecast**: Provide a brief overview of the weather forecast, highlighting key aspects such as temperature variations, precipitation likelihood, and wind conditions.

2. **Recommendation based on the Weather**: Offer a recommendation tailored to the forecasted weather conditions. This could include suggestions on whether to dress warmly, prepare for rain, or expect sunny weather.

3. **Suggestions on What to Wear**: Based on the weather forecast and the user's preferences, propose suitable clothing options for the day. This should include a complete outfit recommendation, taking into account factors like warmth, comfort, style, and specific clothing items, colors, and styles.

Please ensure that your message is informative, engaging, and user-friendly, providing valuable guidance to users as they plan their attire for the day. The weather forecast will be provided in the JSON format specified below:

```json
{
    "city": {
        "coord": {
            "lat": 32.0853,
            "lon": 34.7818
        },
        "country": "IL",
        "id": 293397,
        "name": "Tel Aviv",
        "population": 250000,
        "sunrise": 1710906264,
        "sunset": 1710949927,
        "timezone": 7200
    },
    "cnt": 8,
    "cod": "200",
    "list": [
        {
            "clouds": {
                "all": 17
            },
            "dt": 1710903600,
            "dt_txt": "2024-03-20 03:00:00",
            "main": {
                "feels_like": 12.93,
                "grnd_level": 1013,
                "humidity": 80,
                "pressure": 1015,
                "sea_level": 1015,
                "temp": 13.44,
                "temp_kf": -0.64,
                "temp_max": 14.08,
                "temp_min": 13.44
            },
            "pop": 0.35,
            "rain": {
                "3h": 0.21
            },
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "light rain",
                    "icon": "10n",
                    "id": 500,
                    "main": "Rain"
                }
            ],
            "wind": {
                "deg": 207,
                "gust": 8.28,
                "speed": 5.58
            }
        },
        {
            "clouds": {
                "all": 25
            },
            "dt": 1710914400,
            "dt_txt": "2024-03-20 06:00:00",
            "main": {
                "feels_like": 14.19,
                "grnd_level": 1015,
                "humidity": 76,
                "pressure": 1017,
                "sea_level": 1017,
                "temp": 14.68,
                "temp_kf": -0.78,
                "temp_max": 15.46,
                "temp_min": 14.68
            },
            "pop": 0.49,
            "rain": {
                "3h": 0.28
            },
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "light rain",
                    "icon": "10d",
                    "id": 500,
                    "main": "Rain"
                }
            ],
            "wind": {
                "deg": 204,
                "gust": 9.3,
                "speed": 7.11
            }
        },
        ... (forecast data continues)
    ],
    "message": 0
}
```

Use this information to craft your response. Ensure that the message provides valuable insights and guidance to users as they plan their attire for the day.

Response Example:
-----------------

Summary of the Forecast:
------------------------
The weather forecast for Tel Aviv in the next 12 hours indicates a mix of conditions. Expect light rain in the early morning, followed by cloudy skies and a gradual clearing later in the day. Temperatures will range from 13°C to 18°C, with a slight breeze from the southwest.

Recommendation based on the Weather:
--------------------------------------
Considering the forecasted conditions, it's advisable to dress in layers to stay comfortable throughout the day. Be prepared for the possibility of rain in the morning but anticipate clearer skies by midday.

Suggestions on What to Wear:
----------------------------
For the morning rain, opt for a waterproof trench coat in a neutral color such as beige, paired with a lightweight sweater underneath. Choose dark wash jeans for a versatile look and complement with ankle boots in a waterproof material. As the day progresses and the weather improves, you can remove the trench coat and layer with a stylish scarf for added warmth. Swap the boots for loafers or sneakers for a more casual feel. Don't forget to accessorize with a classic umbrella to stay dry in case of unexpected showers.

Example Complete Outfit:
------------------------
Morning: Beige trench coat, lightweight sweater, dark wash jeans, ankle boots, stylish scarf, classic umbrella.
Afternoon: Lightweight sweater, dark wash jeans, loafers or sneakers.
Accessories: Classic umbrella.
"""
)


def generate_clothing_recommendations(weather_forecast, user_preferences):
    # Create a copy of the weather forecast
    combined_dict = weather_forecast.copy()

    # Update the copy with user preferences
    combined_dict.update(user_preferences)

    # Convert the combined dictionary to a string
    user_input_string = json.dumps(combined_dict)

    recommendations = process_interaction(user_input=user_input_string, system_message=SYSTEM_MESSAGE)

    # Log the recommendations
    current_app.logger.info(f"recommendations: {recommendations}")

    return recommendations
