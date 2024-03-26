import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')
LOG_FILE = 'logs/app.log'

OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_ORGANIZATION = os.environ.get('OPENAI_ORGANIZATION')
