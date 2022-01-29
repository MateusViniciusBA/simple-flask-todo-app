from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ozama@123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debug.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def init_db():
    db.create_all()

from .views import *
from .controllers import *
