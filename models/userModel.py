from flask_sqlalchemy import SQLAlchemy
from app import app,db



class Users(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True)
    phone = db.Column(db.String(100), unique = True)


def __init__(self,name,email,phone):
    self.name = name
    self.email = email
    self.phone = phone

with app.app_context():
    db.create_all()