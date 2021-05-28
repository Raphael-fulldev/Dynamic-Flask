from app import app, db
from app.models import Subscription

@app.shell_context_processor #pre-import to shell session | If doesn't work: set FLASK_APP=app.py
def make_shell_context():
    return {'db': db, 'Subscription': Subscription}

#set FLASK_DEBUG=1