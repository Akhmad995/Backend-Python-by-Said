from flask import Flask
from flask import url_for, request
from flask import render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    params = {}
    params['title'] = 'Главная страница'

    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/news', methods=['GET', 'POST'])
def news():

    if request.method == 'POST':
        con = sqlite3.connect('home-work2/db/db-news.db')
        cursor = con.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS news(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(200),
            text VARCHAR(200)
        );
        """)
       
        news_query = "INSERT INTO news(title, text) VALUES(?, ?)"
       
        news_data = [
            ( str(request.form.get('title')), str(request.form.get('text')) )
        ]
        cursor.executemany(news_query, news_data)

        con.commit()
        cursor.close()
        con.close()


        return render_template('news.html')
    
    else:

        con = sqlite3.connect('home-work2/db/db-news.db')
        cursor = con.cursor()


        cursor.execute("SELECT * FROM news")

        news = cursor.fetchall()

        con.commit()
        cursor.close()
        con.close()


        return render_template('news.html', news = news)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
