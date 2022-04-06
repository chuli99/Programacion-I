import sqlite3
from models import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_Id = db.Column(db.Integer, nullable= False)
    poem_Id = db.columb(db.Integer, nullable= False)
    qualifications = db.columb(db.Integer, nullable = False)
    comment = db.column(db.string(100), nullable = False)
    