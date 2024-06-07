from flask import Flask
from flask_bootstrap import Bootstrap4
import os 
from dotenv import load_dotenv
load_dotenv(override=True)

def create_app():
    app = Flask(__name__)
    Bootstrap4(app)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from .routes import bp
    app.register_blueprint(bp)

    return app
