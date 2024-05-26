from flask import Flask, current_app
from config import Config
import os
import logging
from logging.handlers import RotatingFileHandler
from flask_bootstrap import Bootstrap4


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    Bootstrap4(app)  # flask-bootstrap
    
    with app.app_context():
        app.debug=current_app.config["DEBUG"]

    # Register blueprints
    from .main import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    # Set up log handler
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    
    # Log app startup message
    with app.app_context():
        app.logger.info('{} startup'.format(current_app.config['APP_NAME']))
    
    return app
