from config import db
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=True)