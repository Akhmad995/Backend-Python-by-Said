# Файл с моделями приложения
from flask_login import UserMixin
from config import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    town_name = db.Column(db.Text, unique=True, nullable=False)
    users = db.relationship('User', backref='user_address')


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.Text, nullable=False)
    tags = db.relationship('Tag', backref='posts', secondary='post_tag')
    

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.Text, nullable=False)


post_tag = db.Table(
    'post_tag',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)