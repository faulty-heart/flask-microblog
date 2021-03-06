from flask import render_template, flash, redirect, url_for
from app import flask_app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm

@flask_app.route('/')
@flask_app.route('/index')
@login_required
def index():
    user = {'username': 'User1'}
    posts = [
        {
            'author': {'username': 'User2'},
            'body': 'Body of post from author User2'
        },
        {
            'author': {'username': 'User3'},
            'body': 'Body of post from author User3'
        }
    ]
    return render_template('index.html', title='Homepage', posts=posts)

@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or pasword!")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@flask_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@flask_app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations! You are now registered user...')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
