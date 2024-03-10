import os

DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')
OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
LOG_FILE = 'logs/app.log'
