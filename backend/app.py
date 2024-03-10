from flask import Flask
from config import settings
from controllers import weather_controller
from utils.logger import setup_logger

app = Flask(__name__)
app.register_blueprint(weather_controller.blueprint)

setup_logger(app)

if __name__ == '__main__':
    app.run(debug=settings.DEBUG)
