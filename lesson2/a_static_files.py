from flask import Flask
from flask import url_for, request
import sqlite3

app = Flask(__name__)

USERS = {
    'Saeed', '123456',
    'Zaga', '111111',
}

@app.route('/', methods=['POST', 'GET'])
def index(username):
    return f"Здравствуйте, {username}"


@app.route('/news')
def show_news():
    return f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Новость</title>

    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
    <h1>Страница новости</h1>

    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Fugiat voluptatem animi corrupti natus nisi, alias ex similique praesentium quae velit quis temporibus numquam molestiae et, placeat mollitia ipsum incidunt necessitatibus.</p>

</body>
</html>
"""

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        # print(request.form.get('login'))
        # print(request.form.get('password'))

        if USERS[request.form.get('login')] == request.form.get('pass'):
            return 'Форма заполнена успешно'
        return "Пароль неверный"
        
    else:
        return '''
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Авторизация</title>
        </head>
        <body>

            <form action="/login" method="post">
                <input type="text" name="login">
                <input type="password" name="pass">
                <input type="submit" value="Авторизоваться">
            </form>
            
        </body>
        </html>
        '''
        



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)