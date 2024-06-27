from flask import Blueprint,render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth=Blueprint('auth',__name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True )

@auth.route('/logout')
def logout():
    return"<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_Name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_Name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif len(password1) < 7:
            flash('Passwords don\'t match.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            flash('Account created!', category='success')
            pass
        
    return render_template("signup.html")



    