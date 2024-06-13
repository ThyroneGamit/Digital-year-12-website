from flask import Blueprint, render_template
from flask_login import login_user, login_required,  current_user

views = Blueprint('views', __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", user=current_user)

@views.route('/sign-up')
def sign_up():
    return render_template("signup.html")
@views.route('/login')
def login():
    return render_template("login.html", boolean=True )







