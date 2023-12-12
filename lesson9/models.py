# Файл с моделями приложения
from config import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    town_name = db.Column(db.Text, unique=True, nullable=False)
    users = db.relationship('User', backref='user_address')

