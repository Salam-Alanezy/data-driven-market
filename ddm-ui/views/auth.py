from flask import Blueprint, render_template, request, redirect, url_for, session
from models import login_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = login_user(email, password)
        
        if user:
            session['email'] = email
            return redirect(url_for('dashboard.index'))
        else:
            return render_template('login.html', error="Login Failed")
    else:
        return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('auth.login'))
