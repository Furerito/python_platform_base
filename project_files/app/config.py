import os
from configparser import ConfigParser
from datetime import timedelta

print('config.py')

# Ermittelt das Verzeichnis, in dem sich das aktuelle Skript befindet
base_dir = os.path.dirname(os.path.abspath(__file__))

# Zusammensetzen des Pfades zur Konfigurationsdatei
config_path = os.path.join(base_dir, '../config.ini')

print(config_path)

config = ConfigParser()
config.read(config_path)

print(config.sections())

class Config:
    SECRET_KEY = config['flask']['secret_key']
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=int(config['flask']['session_timeout']))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONFIG = {
        'host': config['database']['host'],
        'database': config['database']['database'],
        'user': config['database']['user'],
        'password': config['database']['password'],
        'port': config['database']['port']
    }
    ISSUER_NAME = config['flask']['issuer_name']
    APP_LOGO = config['app']['logo']
    PORT = int(config['flask']['port'])
    STATIC_FOLDER = config['flask']['static_folder']