# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
from config.settings import Config 
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, views, controllers