from flask import render_template, redirect, url_for

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, current_user, logout_user, login_required

from config import app, db, login_manager
from models import User
from forms import UserForm, LoginForm


@login_manager.user_loader
def load_user(user_id):
    # db_sess = db.session.create_session()
    # return db_sess.query(User).get(user_id)
    return User.query.get(user_id)


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = LoginForm()

    username = login_form.username.data
    password = login_form.password.data
    user = User.query.filter_by(username=username).first()
        

    if user and check_password_hash(user.hashed_password, password):
        login_user(user)
        return redirect( url_for('user_info') )


    return render_template('index.html', form=login_form)


@app.route('/user_info')
def user_info():
    return f"Здравствуйте, {current_user.username}"
    # return render_template('user_info.html')

@app.route('/logaut')
def logaut():
    logout_user()
    return  redirect( url_for('index') )


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    userForm = UserForm()
    if userForm.validate_on_submit():
        username = userForm.username.data
        password = userForm.password.data
        # Считанное с формы значение пароля захешируем.
        hashed_password = generate_password_hash(password)
        # Создадим объект пользователя с хешем вместо пароля.
        user = User(
            username=username,
            hashed_password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
    users = User.query.all()
    return render_template('users.html', form=userForm, users=users)


# Обработчик ошибки 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


# Обработчик ошибки 403
@app.errorhandler(403)
def not_permitted(error):
    return render_template('403.html', error=error), 403

# Обработчик ошибки 403
@app.errorhandler(401)
def not_permitted(error):
    return render_template('401.html', error=error), 401


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
