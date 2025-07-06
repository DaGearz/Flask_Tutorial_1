from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    return render_template("login.html", text = "Testing", user = "Todd")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form['email']
        firstname = request.form['firstName']
        password1 = request.form['password1']
        password2 = request.form['password2']

        if len(email) < 4:
            flash("Email must be at least 4 characters", category="error")
            pass
        elif len(firstname) < 3:
            flash("First name must be at least 3 characters", category="error")
            pass
        elif password1 != password2:
            flash("Passwords don't match", category="error")
            pass
        elif len(password1) < 7:
            flash("Password must be atleast 7 chars")
            pass
        else:
            flash("Login Successful", category="success")
            #add user to database
            pass


    return render_template("sign_up.html")

@auth.route('/logout')
def logout():
    return "<p>Logged out</p>"
