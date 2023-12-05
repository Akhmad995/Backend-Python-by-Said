import os

from flask import Flask
from flask import render_template, redirect

from flask import render_template, request, redirect, url_for
from flask_migrate import Migrate

from config import db, app
from models import Post
from forms import PostForm

from flask_wtf.csrf import CSRFProtect

migrate = Migrate(app, db)

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('MY_SECRET_KEY')

app.config["SECRET_KEY"] = SECRET_KEY
csrf = CSRFProtect(app)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST', 'GET'])
def add_post():
    if request.method == "POST":
        postform = PostForm()

        if postform.validate_on_submit():
            title = postform.title.data
            text = postform.text.data
            author = postform.author.data
            post = Post(title=title, text=text, author=author)

            db.session.add(post)
            db.session.commit()
            print(post)
    
    posts = Post.query.all()
    return render_template('post.html', posts=posts, form=postform)


@app.route('/posts/<int:post_id>')
def get_post(post_id):
    post = Post.query.get_or_404(post_id)

    return render_template('single_post.html', post=post)


@app.route('/posts/author/<string:author_name>')
def get_author(author_name):
    posts = Post.query.filter_by(author=author_name).all()

    return render_template('author_posts.html', posts=posts)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)