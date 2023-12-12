from flask import render_template, request, redirect
from flask_migrate import Migrate

from flask_wtf.csrf import CSRFProtect

from config import app, db
from models import User, Address
from forms import UserForm, AddressForm

migrate = Migrate(app, db)

SECRET_KEY = 'Мой секретный ключ'
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)


@app.route('/')
def index():
    users = User.query.all()

    town = Address.query.filter_by(town_name = 'Махачкала').first()
    user1 = User(username='Магомед', address_id=town.id)
    print(user1.username, user1.address_id)
    
    # town1 = Address(town_name='Москва')
    # town2 = Address(town_name='Хасавюрт')
    # db.session.add(town1)
    # db.session.add(town2)

    # user2 = User(username='Гасейн', address_id=2)
    # user3 = User(username='Сидреддин', address_id=2)
    # db.session.add(user2)
    # db.session.add(user3)

    # db.session.commit()

    user2 = User.query.get(1)
    address = Address.query.get(1)

    print(user2.user_address.town_name)
    
    print("*****")

    for user in address.users:
        print(user.username)


    return render_template('index.html', users = users)


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
