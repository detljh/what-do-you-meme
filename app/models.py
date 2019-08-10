from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    coin = db.Column(db.Integer, default=0)
    memes = db.relationship('MemeCard', backref='author', lazy='dynamic')
    
class MemeCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meme_image = db.Column(db.String(128))
    description = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))