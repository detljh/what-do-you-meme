from flask import *
from app import app
from app.scraper import NewsScraper
from app.forms import LoginForm
from app.models import *
from config import Config
import os
import time
import random

post_number = 0
scraper = NewsScraper()
title, content = scraper.scrape_headline_title(), scraper.scrape_content()

@app.route('/', methods=['GET', 'POST'])
def login():
    image = "/static/images/intro.jpg"
    return render_template('login.html', title="Meme the news", image_src=image)

@app.route('/start', methods=['GET', 'POST'])
def start():
    scraper = NewsScraper()
    title, content = scraper.scrape_headline_title(), scraper.scrape_content()
    if post_number >= len(title):
        return redirect("/end")
    
    return render_template("start.html", src_happy=get_image('happy'), src_sad=get_image('sad'), src_angry=get_image('angry'), \
    src_shocked=get_image('shocked'), src_thinking=get_image('thinking'), skip="/static/images/skip.png", article=[title[post_number], content[post_number]])

def get_image(type):
    image_dir = os.listdir(os.path.join(Config.IMAGE_FOLDER, type))
    image = '/static/images/' + type + '/' + random.choice(image_dir)
    return image

@app.route('/increment', methods=["GET", "POST"])
def increment():
    global post_number
    post_number += 1
    return redirect(url_for("start"))

@app.route('/end', methods=['GET', 'POST'])
def end():
    return render_template("end.html")

