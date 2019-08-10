from flask import *
from app import app

@app.route('/', methods=['GET', 'POST'])
def login():

    return render_template('entry_page.html', title="Start reading!", form=form)
