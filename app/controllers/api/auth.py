from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from app import db, google
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login/google')
def login_google():
    return google.authorize(callback=url_for('auth.google_authorized', _external=True))

@auth.route('/login/google/callback')
def google_authorized():
    response = google.authorized_response()
    if response is None or response.get('access_token') is None:
        flash('A autenticação via Google falhou.', 'danger')
        return redirect(url_for('auth.login'))

    google_user_info = google.get('userinfo')
    user = User.query.filter_by(email=google_user_info.data['email']).first()

    if user is None:
        # Crie um novo usuário para o login via Google
        user = User(email=google_user_info.data['email'])
        db.session.add(user)
        db.session.commit()

    login_user(user, True)
    return redirect(url_for('index'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # Implemente a lógica para cadastro de e-mail/senha
    return render_template('signup.html')
