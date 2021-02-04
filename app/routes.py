from flask import render_template
from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'User1'}
    return render_template('index.html', title='Homepage', user=user)
    