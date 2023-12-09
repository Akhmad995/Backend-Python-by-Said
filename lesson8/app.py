from flask import render_template, request, redirect
from flask_migrate import Migrate

from flask_wtf.csrf import CSRFProtect

from config import app, db
from models import User
from forms import UserForm

migrate = Migrate(app, db)

SECRET_KEY = 'Мой секретный ключ'
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


# Работа со страницей списка всех авторов, подходящих по условию
@app.route('/users', methods=['GET', 'POST'])
def get_users():
    userform = UserForm()

    if userform.validate_on_submit():
        username = userform.username.data
        age = userform.age.data
        address = userform.address.data
        user = User(username=username, age=age, address=address)

        db.session.add(user)
        db.session.commit()

    users = User.query.all()

    return render_template('users.html', form=userform, users=users)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)
