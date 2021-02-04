from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'User1'}
    return '''
    <html>
        <head>
            <title>Homepage - Microblog</title>
        </head>
        <body>
            <h1>Hello ''' + user['username'] + '''!</h1>
        </body
    </html>'''