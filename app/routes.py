from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm

@app.route("/")
def index():
    user_dict = {
        'username': 'Jamie',
        'email': 'jamie@codingtemple.com'
    }
    colors = ['red', 'blue', 'purple', 'green', 'orange']
    return render_template('index.html', user=user_dict, colors=colors)


@app.route('/signup')
def signup():
    