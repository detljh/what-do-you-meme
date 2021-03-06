from app import db
from werkzeug.security import *

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    coin = db.Column(db.Integer, default=0)
    memes = db.relationship('MemeCard', backref='author', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
class MemeCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meme_image = db.Column(db.String(128))
    description = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class HappyMeme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(300))
    
class Stat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_tag = db.Column(db.String(20), unique=True)
    happy = db.Column(db.Integer, default=0)
    sad = db.Column(db.Integer, default=0)
    angry = db.Column(db.Integer, default=0)
    shocked = db.Column(db.Integer, default=0)
    thinking = db.Column(db.Integer, default=0)
    