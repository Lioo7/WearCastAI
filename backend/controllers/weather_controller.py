from flask import Blueprint, jsonify, request, abort
from services.weather_service import fetch_weather_data_by_coordinates, fetch_weather_data_by_city

blueprint = Blueprint('weather', __name__, url_prefix='/api/v1')


# example: http://127.0.0.1:5000/api/v1/weather-by-coordinates?latitude=32.085300&longitude=34.781769#
@blueprint.route('/weather-by-coordinates', methods=['GET'])
def get_weather_by_coordinates():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if not latitude or not longitude:
        abort(400, 'Missing required parameters')

    weather_data = fetch_weather_data_by_coordinates(latitude, longitude)
    if weather_data is None:
        abort(404, 'Failed to fetch weather data')

    return jsonify(weather_data), 200


# example: http://127.0.0.1:5000/api/v1/weather-by-city?city=Tel-Aviv
@blueprint.route('/weather-by-city', methods=['GET'])
def get_weather_by_city():
    city = request.args.get('city')

    if not city:
        abort(400, 'Missing required parameter')

    weather_data = fetch_weather_data_by_city(city)
    if weather_data is None:
        abort(404, 'Failed to fetch weather data')

    return jsonify(weather_data), 200
