from flask import Blueprint, jsonify, request, abort
# from services.weather_service import fetch_weather_data_by_coordinates

blueprint = Blueprint('weather', __name__, url_prefix='/api/v1')


@blueprint.route('/')
def hello_world():
    return "Hello World!"


# @blueprint.route('/weather-by-coordinates', methods=['GET'])
# def get_weather_by_coordinates():
#     latitude = request.args.get('latitude')
#     longitude = request.args.get('longitude')

#     if not latitude or not longitude:
#         abort(400, 'Missing required parameters')

#     weather_data = fetch_weather_data_by_coordinates(latitude, longitude)
#     if weather_data is None:
#         abort(404, 'Failed to fetch weather data')

#     return jsonify(weather_data), 200

# Other endpoints implementation...
