from flask import *
from app import app
from app.forms import LoginForm
from app.models import *
from config import Config
import os


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', title="Sign in", form=form)

@app.route('/home', methods=['GET', 'POST'])
def home():
    filepath = "/static/images/happy/dicaprio3-583e33155f9b58d5b19e3a00.jpg"
    return render_template('home.html', src=filepath, article="news article")
