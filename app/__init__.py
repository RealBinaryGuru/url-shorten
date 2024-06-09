from flask import Flask
import os 
from dotenv import load_dotenv
load_dotenv(override=True)

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from .routes import bp
    app.register_blueprint(bp)

    return app
