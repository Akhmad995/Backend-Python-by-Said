from  flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'all_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(88), unique=True, nullable=False)
    # Распространные типы - Integer, Text, Boolean, Datetime, Float, LargeBinary


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get("username")
    user = User(username=username)
    db.session.add(user)
    db.session.commit()

    return redirect( url_for('index') )



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)