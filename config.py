import os
from pymongo import MongoClient


class Config:
    # Application
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    TEMPLATES_DIR = os.path.join(APP_DIR, 'view')
    STATIC_DIR = os.path.join(APP_DIR, 'view', 'static')
    LOGFILE = os.path.join(APP_DIR, 'flask.log')
    DEBUG = True
    FLASK_SECRET = 'the-most-secret-key-in-the-secret-world-of-secret-keys'

    DB_NAME = 'timesheet'
    JWT_SECRET = 's3cr3t-jwt-k3y-h3h3'
