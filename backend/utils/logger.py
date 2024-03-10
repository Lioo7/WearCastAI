import logging
from logging.handlers import RotatingFileHandler
from flask import request
from config import settings


def setup_logger(app):
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    file_handler = RotatingFileHandler(settings.LOG_FILE, maxBytes=10000, backupCount=1)
    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

    @app.before_request
    def log_request_info():
        app.logger.info(f'Request: {request.method} {request.path} {request.data}')

    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(f'Error: {str(e)}')
        return jsonify({'error': 'An error occurred'}), 500
