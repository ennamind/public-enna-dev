# contains the configuration variables for your application

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///myapp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
