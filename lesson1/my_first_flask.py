# Фреймворк FLASK

# pip install flask
# CGI
# WSGI
# Werkzeug
# Jinja2
# Flask

# https://flask-russian-docs.readthedocs.io/ru/master/


# Создаем простое приложение
from flask import Flask
from flask import request


app = Flask(__name__) # Создается объект приложения

@app.route("/") # декоратор, определяющий URL
@app.route("/index")
def hello_world():
    return "Привет, мир!" # Flask преобразует строку в объект ответа

@app.route("/about")
def about_us():
    return "<h1>Страница о нас</h1>"

@app.route("/news")
def news():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Страница новости</title>
</head>
<body>

    <h1>Новость 1</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam labore dolores eaque est earum soluta molestias doloremque fugit. Cum dolorum in reprehenderit ducimus ullam fuga facilis voluptatum vel laudantium sequi!</p>
    
</body>
</html>
'''

@app.route('/users/<username>') # Задаем параметр через который передаем информацию
def show_user(username):
    return f"Пользователь с id = {username}"

@app.route('/posts/<int:id>') # явное обозначение типа параметра - int, float, string
def show_post(id):
    return f"Публикация № {id}"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
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
                <input type="password" name="password">
                <input type="submit" value="Авторизоваться">
            </form>
            
        </body>
        </html>
        '''
    else:
        return '''
                <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Админка</title>
            </head>
            <body>

                <h1>Вы авторизовались</h1>
                
            </body>
            </html>
            '''
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

