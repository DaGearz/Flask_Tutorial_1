from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from website.models import Note, User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login Successful',category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Login Unsuccessful', category='error')
        else:
            flash('email does not exist', category = 'error')


    return render_template("login.html", user=current_user)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form['email']
        firstname = request.form['firstName']
        password1 = request.form['password1']
        password2 = request.form['password2']
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already registered', category = 'error')
        elif len(email) < 4:
            flash("Email must be at least 4 characters", category="error")
        elif len(firstname) < 3:
            flash("First name must be at least 3 characters", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 chars")
        else:
            new_user = User(email=email, first_name=firstname, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            flash("Login Successful", category="success")
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account Created", category="success")
            return redirect(url_for('views.home'))



    return render_template("sign_up.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
