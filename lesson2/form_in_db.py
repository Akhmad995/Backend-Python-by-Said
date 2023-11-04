from flask import Flask
from flask import url_for, request
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return "Привет, мир!"



@app.route('/registr', methods=['POST', 'GET'])
def registr():
    if request.method == 'POST':

        con = sqlite3.connect('lesson2/db/db_user.db')
        cursor = con.cursor()

        #cursor.execute("DROP TABLE users")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login VARCHAR(200),
            pass VARCHAR(200)
        );
        """)
       
        users_query = "INSERT INTO users(login, pass) VALUES(?, ?)"
       
        users_data = [
            ( str(request.form.get('login')), str(request.form.get('pass')), )
        ]
        cursor.executemany(users_query, users_data)

        con.commit()
        cursor.close()
        con.close()

        return "Регистрация прошла!"
        
    else:

        return f'''
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Регистрация</title>

            <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>

            <form action="/registr" method="post">
                <div>
                    <input type="text" name="login" placeholder="Логин">
                </div>
                <div>
                    <input type="password" name="pass" placeholder="Пароль">
                </div>
                <input type="submit" value="Регистрация">
            </form>
            
        </body>
        </html>
        '''
        

@app.route('/auth', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        con = sqlite3.connect('lesson2/db/db_user.db')
        cursor = con.cursor()

        cursor.execute(f"SELECT * FROM users WHERE login = '{str(request.form.get('login'))}'")

        print(cursor.fetchall())

        con.commit()
        cursor.close()
        con.close()

        return "Вы авторизованы!"
        
    else:

        return f'''
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Авторизация</title>

            <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>

            <form action="/auth" method="post">
                <div>
                    <input type="text" name="login" placeholder="Логин">
                </div>
                <div>
                    <input type="password" name="pass" placeholder="Пароль">
                </div>
                <input type="submit" value="Авторизация">
            </form>
            
        </body>
        </html>
        '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)