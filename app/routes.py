from flask import *
from app import app
from app.scraper import NewsScraper
from app.forms import LoginForm
from app.models import *
from config import Config
import os
import time
import random

tags = {
    "crime": ["killed", "murder", "kidnap", "blood", "abduction", "abducted", "rape", "crash", "accident", "blast", "abuse", "beat", "chase", "gun", "jail", "prison", "punishment", "raid", "weapon"],
    "calamity": ["floods", "typhoon", "tornado", "earthquake", "volcano", "cyclone", "wind", "turbulence", "dead", "windy"],
    "politics": ["trump", "us", "china", "uk", "govt", "hong kong", "yemen", "aden"],
}


post_number = 0
scraper = NewsScraper()
title, content = scraper.scrape_headline_title(), scraper.scrape_content()

@app.route('/', methods=['GET', 'POST'])
def login():
    image = "/static/images/intro.jpg"
    return render_template('login.html', title="Meme the news", image_src=image)

@app.route('/start', methods=['GET', 'POST'])
def start():
    for s in Stat.query.all():
        print(s.news_tag, s.happy, s.sad, s.angry, s.shocked, s.thinking)
    scraper = NewsScraper()
    title, content = scraper.scrape_headline_title(), scraper.scrape_content()
    if post_number >= len(title):
        return redirect("/end")
        
    for k,v in tags.items():
        for values in v:
            if values in content[post_number].lower() or values in title[post_number].lower():
                news_tag = k
                return render_template("start.html", src_happy=get_image('happy'), src_sad=get_image('sad'), src_angry=get_image('angry'), \
                    src_shocked=get_image('shocked'), src_thinking=get_image('thinking'), article=[title[post_number], content[post_number], news_tag])
    
    # tokens = nlp(title[post_number])
    # doc = list(map(lambda x: x.text, filter(lambda x: x.pos_ in ["NOUN", "PROPN", "VERB"], tokens)))
    # tag = "NONE"
    # for key in tags.keys():
    #     print(key)
    #     for i in range(len(doc)):
    #         if doc[i].lower() in tags[key]:
    #             tag = key
    #             return render_template("start.html", src_happy=get_image('happy'), src_sad=get_image('sad'), src_angry=get_image('angry'), \
    #             src_shocked=get_image('shocked'), src_thinking=get_image('thinking'), article=[title[post_number], content[post_number], tag])
    return render_template("start.html", src_happy=get_image('happy'), src_sad=get_image('sad'), src_angry=get_image('angry'), \
    src_shocked=get_image('shocked'), src_thinking=get_image('thinking'), article=[title[post_number], content[post_number], "None"])

def get_image(type):
    image_dir = os.listdir(os.path.join(Config.IMAGE_FOLDER, type))
    image = '/static/images/' + type + '/' + random.choice(image_dir)
    return image

@app.route('/increment/<react_type>/<tag>', methods=["GET", "POST"])
def increment(react_type, tag):
    global post_number
    post_number += 1
    
    if react_type != None and tag != None:
        s = Stat.query.filter_by(news_tag=tag).first()
        new = False
        
        if s is None:
            new = True
            
        if react_type == 'happy':
            if new:
                s = Stat(news_tag=tag, happy=1)
                
            else:
                s.happy += 1
                
        elif react_type == 'sad':
            if new:
                s = Stat(news_tag=tag, sad=1)
                
            else:
                s.sad += 1
        elif react_type == 'angry':
            if new:
                s = Stat(news_tag=tag, angry=1)
                
            else:
                s.angry += 1
        elif react_type == 'shocked':
            if new:
                s = Stat(news_tag=tag, shocked=1)
                
            else:
                s.shocked += 1
        elif react_type == 'thinking':
            if new:
                s = Stat(news_tag=tag, thinking=1)
                
            else:
                s.thinking += 1
        
        if new:
            db.session.add(s)
        
        db.session.commit()
                
    return redirect(url_for("start"))

@app.route('/end', methods=['GET', 'POST'])
def end():
    stats = Stat.query.all()
    return render_template("end.html", stats=stats)

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    global post_number
    post_number = 0
    return redirect(url_for("start"))
    

