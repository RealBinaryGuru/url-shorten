import os
from dotenv import load_dotenv, dotenv_values

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
cnf = dotenv_values()

class Config(object):
    APP_NAME = os.environ.get('APP_NAME','URL Shortener')
    DEBUG = os.environ.get('FLASK_DEBUG', False)