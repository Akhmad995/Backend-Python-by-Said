from flask import render_template, request, redirect
from flask_migrate import Migrate
from flask_login import login_manager

from flask_wtf.csrf import CSRFProtect

from config import app, db
from models import User, Address, Post, Tag
from forms import UserForm, AddressForm

migrate = Migrate(app, db)

SECRET_KEY = 'Мой секретный ключ'
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

login_manager = LoginManager(app)


@app.login_manager().user_loader
def load_user(user_id):
    db_sess = db.session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    users = User.query.all()

   
    # post1 = Post(post_name = 'Название 1')
    # post2 = Post(post_name = 'Название 2')

    # db.session.add(post1)
    # db.session.add(post2)


    # tag1 = Tag(tag_name = 'Тег 1')
    # tag2 = Tag(tag_name = 'Тег 2')

    # db.session.add(tag1)
    # db.session.add(tag2)


    # post1 = Post.query.get_or_404(1, "Такого нет")

    # tag1 = Tag.query.get_or_404(1)
    # tag2 = Tag.query.get_or_404(2)

    # post1.tags.append(tag1)
    # post1.tags.append(tag2)

    # print(post1.tags)
    # print(tag1.posts)

    db.session.commit()

    return render_template('index.html', users = users)

@app.errorhandler(404)
def page_not_found(error):
    return  render_template('404.html', error = error), 404

# Работа со страницей списка всех авторов, подходящих по условию
@app.route('/users', methods=['GET', 'POST'])
def get_users():
    userform = UserForm()

    if userform.validate_on_submit():
        username = userform.username.data
        address = userform.address.data
        user = User(username=username, address_id=address)

        db.session.add(user)
        db.session.commit()

    users = User.query.all()

    return render_template('users.html', form=userform, users=users)


@app.route('/towns', methods=['GET', 'POST'])
def get_towns():
    addressform = AddressForm()

    if addressform.validate_on_submit():
        town_name = addressform.town_name.data
        town = Address(town_name=town_name)

        db.session.add(town)
        db.session.commit()

    towns = Address.query.all()

    return render_template('towns.html', form=addressform, towns=towns)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)
