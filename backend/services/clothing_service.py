import json
from flask import current_app

from .chat_gpt_service import process_interaction

# Constant for system message
SYSTEM_MESSAGE = (
    """
    Your objective is to design a JSON-based weather forecasting and clothing recommendation system for users. The system should provide personalized clothing suggestions based on the weather forecast and the user's individual preferences, such as cold tolerance, style, age, and gender.

    The JSON object should include the following components:

    1. Forecast Summary:
    - Provide a concise overview of the weather forecast, highlighting key details such as temperature ranges, precipitation likelihood, wind conditions, and any significant weather events.

    2. Weather Recommendations:
    - Offer tailored advice based on the forecasted weather conditions, guiding users on appropriate attire for the day.
    - Consider factors like the user's sensitivity to cold or warm temperatures, as well as the weather trends throughout the day (e.g., morning rain, clearing skies in the afternoon).

    3. Clothing Suggestions:
    - Recommend suitable clothing options for both morning and evening, taking into account factors such as warmth, comfort, style, specific garments, colors, and fashion preferences.
    - Provide distinct recommendations for morning and evening, as the weather and user's needs may differ.

    The user will provide a JSON file with the following keys:

    - `weather_forecast`: Includes the complete weather forecast for the day, obtained from the 'OpenWeatherMap' API.
    - `user_preferences`: Consists of the user's preferences, including gender, age, style, and cold tolerance, represented as a dictionary.

    The system should incorporate this information to offer valuable insights and guidance to users as they plan their attire for the day.

    Response Example:
    {
        "forecast": {
            "summary": "Mixed conditions with light rain early, followed by cloudy skies gradually clearing. Temperature range: 13-18°C. A gentle breeze from the southwest.",
            "recommendation": "Dress in layers to adapt to the changing weather. Expect rain in the morning, but clearer skies by midday."
        },
        "clothing_suggestions": {
            "morning": [
                "Wear a button-down shirt in a neutral tone with dark-wash jeans.",
                "Add a lightweight jacket or hoodie that can be easily removed."
            ],
            "evening": [
                "Opt for a graphic t-shirt or polo shirt in a bold color or pattern, with jeans.",
                "Finish the look with a lightweight, casual jacket or sweater."
            ]
        }
    }
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
