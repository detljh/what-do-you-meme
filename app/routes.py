from flask import *
from app import app
from app.scraper import NewsScraper
from app.forms import LoginForm
from app.models import *
from config import Config
import os
import time

post_number = 0
scraper = NewsScraper()
title, content = scraper.scrape_headline_title(), scraper.scrape_content()

@app.route('/', methods=['GET', 'POST'])
def login():
    image = "/static/images/intro.jpg"
    return render_template('login.html', title="Meme the news", image_src=image)

@app.route('/start', methods=['GET', 'POST'])
def start():
    filepath = "/static/images/intro.jpg"
    if post_number >= len(title):
        return redirect("/end")
    return render_template("start.html", src=filepath, article=[title[post_number], content[post_number]])

@app.route('/increment', methods=["GET", "POST"])
def increment():
    global post_number
    post_number += 1
    return redirect(url_for("start"))

@app.route('/end', methods=['GET', 'POST'])
def end():
    return render_template("end.html")