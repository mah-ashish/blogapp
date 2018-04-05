from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    posts = [
    {'username':'amy', 'body':"In town tomorrow!!"},
    {'username':'emily', 'body':"Any plans for weekend?"},
    {'username':'phoebe', 'body':'game night is on!!'}
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)
