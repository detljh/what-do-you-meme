from flask import *
from app import app
from app.scraper import NewsScraper
from app.forms import LoginForm
from app.models import *
from config import Config
import os
import time

post_number = 0

@app.route('/', methods=['GET', 'POST'])
def login():
    image = "/static/images/intro.jpg"
    return render_template('login.html', title="Meme the news", image_src=image)

@app.route('/start', methods=['GET', 'POST'])
def start():
    filepath = "/static/images/intro.jpg"
    scraper = NewsScraper()
    title, content = scraper.scrape_headline_title(), scraper.scrape_content()
    return render_template("start.html", src=filepath, article=[title[0], content[0]])
