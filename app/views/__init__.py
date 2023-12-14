from flask import render_template
# from app.models import UserRepository
from app import app

@app.route('/')
def index():
    # users = UserRepository.get_all_users()
    return render_template('login.html')

@app.route('/signup')
def signup():
    # users = UserRepository.get_all_users()
    return render_template('signup.html')
