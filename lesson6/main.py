from flask import render_template, request, redirect, url_for
from flask_migrate import Migrate

from config import db, app
from models import User, Post

migrate = Migrate(app, db)


@app.route('/')
def index():
    users = User.query.all()
    print(users)
    return render_template('index.html', users=users)


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get("username")
    usersurname = request.form.get("usersurname")
    user = User(username=username, usersurname=usersurname)
    db.session.add(user)
    db.session.commit()
    print(user)

    return redirect( url_for('index') )


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.String, nullable=False)


@app.route('/post', methods=['POST', 'GET'])
def add_post():
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        
        post = Post(title=title, text=text)
        
        db.session.add(post)
        db.session.commit()
        print(post)

        return redirect( url_for('add_post') )
    posts = Post.query.all()
    return render_template('post.html', posts=posts)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)