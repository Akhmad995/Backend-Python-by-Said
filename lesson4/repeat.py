from flask import Flask
from flask import url_for, request
from flask import render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
