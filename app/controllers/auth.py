# from flask import Blueprint, render_template, request, redirect, url_for, flash
# from flask_login import login_user, logout_user, current_user
# from werkzeug.security import check_password_hash

# from models import User
# from app import db, login_manager

# auth_controller = Blueprint('auth', __name__)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# @auth_controller.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()

#         if user and check_password_hash(user.password, password):
#             login_user(user)
#             flash('Login realizado com sucesso!', 'success')
#             return redirect(url_for('index'))

#         flash('Credenciais inválidas. Tente novamente.', 'error')

#     return render_template('login.html')

# @auth_controller.route('/logout')
# def logout():
#     logout_user()
#     flash('Logout realizado com sucesso!', 'success')
#     return redirect(url_for('index'))
