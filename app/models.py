from email.policy import default
from .app import db

from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String(255), nullable=False)
    state = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Todo %r>' % self.name

    def __init__(self, name, desc=''):
        self.name = name
        self.desc = desc