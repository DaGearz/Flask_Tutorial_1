from flask import Blueprint, render_template, request, redirect, url_for, session

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", text = "Testing", user = "Todd")


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

