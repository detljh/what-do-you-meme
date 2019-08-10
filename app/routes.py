from flask import *
from app import app
from app.forms import LoginForm
from app.models import *
from config import Config
import os


@app.route('/', methods=['GET', 'POST'])
def login():
    #form = LoginForm()
    image = "/static/images/intro.jpg"
    return render_template('login.html', title="Meme the news", image_src=image)

# @app.route('/home', methods=['GET', 'POST'])
# def home():
#     h = HappyMeme(image_path=HAPPY_IMAGE_PATH + 'dicaprio3-583e33155f9b58d5b19e3a00.jpg')
#     db.session.add(h)
#     db.session.commit()
#     file_path = HappyMeme.query.get(1).image_path
#     filepath = "/static/images/happy/dicaprio3-583e33155f9b58d5b19e3a00.jpg"
#     return render_template('home.html', src=filepath)

@app.route('/start', methods=['GET', 'POST'])
def start():
    filepath = "/static/images/intro.jpg"
    return render_template("start.html", src=filepath, article="news article")
