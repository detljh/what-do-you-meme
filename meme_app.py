from app import app, db
from app.models import User, MemeCard

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'MemeCard':MemeCard}

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=8080)