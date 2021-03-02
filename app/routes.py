from flask import render_template
from app import flask_app
from app.forms import LoginForm

@flask_app.route('/')
@flask_app.route('/index')
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
    return render_template('index.html', title='Homepage', user=user, posts=posts)

@flask_app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
