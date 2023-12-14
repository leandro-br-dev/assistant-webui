# app/__init__.py

from flask import Flask, redirect, url_for, session, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_oauthlib.client import OAuth

app = Flask(__name__)
from config.settings import Config 
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
oauth = OAuth(app)

from app.models import User  

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Configuração para login com Google
google = oauth.remote_app(
    'google',
    consumer_key=app.config['GOOGLE_CLIENT_ID'],
    consumer_secret=app.config['GOOGLE_CLIENT_SECRET'],
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)



from app import models, views, controllers

from app.controllers.api import api

app.register_blueprint(api, url_prefix='/api')

