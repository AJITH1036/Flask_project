from flask_sqlalchemy import SQLAlchemy
from app import app,db



class Products(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    description = db.Column(db.String(100))


def __init__(self,name,price,description):
    self.name = name
    self.price = price
    self.description = description

with app.app_context():
    db.create_all()