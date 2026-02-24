from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(150), nullable = False)

class Vehicule(db.Model):
    __tablename__ = 'vehicules'
    id = db.Column(db.Integer, primary_key = True)
    brand = db.Column(db.String(100), nullable = False)
    model = db.Column(db.String(100), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    kilometers = db.Column(db.Integer, nullable = False)
    color = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Float, nullable = False)

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    identification_number = db.Column(db.String(50), unique = True, nullable = False)
    phone = db.Column(db.String(20), nullable = False)

