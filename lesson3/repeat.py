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
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

