from flask import *
from app import app
from app.forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    return render_template('login.html', title="Sign in", form=form)