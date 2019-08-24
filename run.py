from app import app
from db import db

db.__init__app(app)

@app.before_first_request
def create_tables():
    db.create_all()