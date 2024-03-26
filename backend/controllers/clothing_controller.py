from flask import Blueprint, request, jsonify, abort, current_app
from services.clothing_service import generate_clothing_recommendations

blueprint = Blueprint('clothing', __name__, url_prefix='/api/v1')


@blueprint.route('/clothing-recommendations', methods=['POST'])
def get_clothing_recommendation():
    # Log the request data
    current_app.logger.info(f"Request Data: {request.get_json()}")

    # Get data from request body
    request_data = request.get_json()

    # Check if required parameters are present
    if 'weather_forecast' not in request_data:
        abort(400, 'Missing required parameter: weather_forecast')
    if 'user_preferences' not in request_data:
        abort(400, 'Missing required parameter: user_preferences')

    # Extract weather forecast and user preferences from request data
    weather_forecast = request_data.get('weather_forecast')
    user_preferences = request_data.get('user_preferences')

    current_app.logger.info(f"weather_forecast: {weather_forecast}")
    current_app.logger.info(f"user_preferences: {user_preferences}")

    # Generate clothing recommendations based on weather forecast and user preferences
    recommendations = generate_clothing_recommendations(weather_forecast, user_preferences)

    # Return recommendations in JSON format
    return jsonify(recommendations), 200
