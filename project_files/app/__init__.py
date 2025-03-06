import os
from configparser import ConfigParser
from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow  
from app.basic_routes import init_basic_routes  

print('__init__.py')

# Ermittelt das Verzeichnis, in dem sich das aktuelle Skript befindet
base_dir = os.path.dirname(os.path.abspath(__file__))

# Zusammensetzen des Pfades zur Konfigurationsdatei
config_path = os.path.join(base_dir, '../config.ini')

config = ConfigParser()
config.read(config_path)

app = Flask(__name__, static_folder=config['flask']['static_folder'])
app.config.from_object(Config)
    
# Konfiguriere die Datenbankverbindung für ORM
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{config['database']['user']}:{config['database']['password']}@{config['database']['host']}/{config['database']['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Initialisiere die Basis Routen für Login und Benutzerverwaltung
# In `app/__init__.py` keine weiteren Logiken platzieren!
init_basic_routes(app, db)