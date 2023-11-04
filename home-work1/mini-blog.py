from flask import Flask
from flask import url_for, request
import sqlite3


app = Flask(__name__)



@app.route('/')
def index():
    return """
        <div><a href="/add">Добавить новость</a></div>
        <div><a href="/search">Поиск новости</a></div>
    """


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':

        con = sqlite3.connect('home-work1/db/db-news.db')
        cursor = con.cursor()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS news(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(200),
            author VARCHAR(200),
            text VARCHAR(200)
        );
        """)
       
        news_query = "INSERT INTO news(title, author, text) VALUES(?, ?, ?)"
       
        news_data = [
            ( str(request.form.get('title')), str(request.form.get('author')), str(request.form.get('text')) )
        ]
        cursor.executemany(news_query, news_data)

        con.commit()
        cursor.close()
        con.close()

        
        return """
            <h2>Новость добавлена.</h2>
            <div><a href="/search">Поиск новости</a></div>
        """
        
    else:

        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Добавить новость</title>

            <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}"/>
        </head>
        <body>
            
            <div id="wrapper">

                <h1>Добавить новость</h1>

                <form class="form" action="/add" method="post">

                    <div>
                        <input class="input" type="text" placeholder="Заголовок" name="title" required/>
                    </div>
                    <div>
                        <input class="input" type="text" placeholder="Автор статьи" name="author" required/>
                    </div>
                    <div>
                        <textarea class="input" placeholder="Текст статьи" name="text" required></textarea>
                    </div>

                    <div class="btns-row">
                        <input class="btn-form" type="submit" value="Добавить"/>
                    </div> <!-- btns-row -->

                </form> <!-- post -->

            </div> <!-- wapper -->

        </body>
        </html>
        '''
        

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':

        con = sqlite3.connect('home-work1/db/db-news.db')
        cursor = con.cursor()


        cursor.execute(f"SELECT * FROM news WHERE author = '{str(request.form.get('search'))}'")

        news_data = cursor.fetchall()

        htmlcode = "";

        for news in news_data:
            htmlcode += f"""
            <div class="news-blck">
                    <figure class="news-img">
                        <img src="{url_for('static', filename='img/noimage.jpg')}" alt="" loading="lazy"/>
                    </figure> <!-- news-img -->
                    
                    <div class="news-content">
                        <div class="news-title">
                            <a href="/{news[0]}">{news[1]}</a>
                        </div> <!-- news-title -->

                        <div class="news-author">{news[2]}</div> <!-- news-author -->
                    </div> <!-- news-content -->
                </div> <!-- news-blck -->
            """


        con.commit()
        cursor.close()
        con.close()

        return f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Поиск новости</title>

                <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}"/>
            </head>
            <body>
                
                <div id="wrapper">

                    <h1>Поиск новости</h1>

                    <form class="form form-search" action="/search" method="post">

                        <div>
                            <input class="input" type="text" placeholder="Поиск статьи по имени автора..." name="search" required/>
                        </div>

                    </form> <!-- post -->

                    <div class="news-list">

                        { str(htmlcode) }

                    </div> <!-- news-list -->


                </div> <!-- wapper -->

            </body>
            </html>
        '''
        
    else:

        return f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Поиск новости</title>

                <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}"/>
            </head>
            <body>
                
                <div id="wrapper">

                    <h1>Поиск новости</h1>

                    <form class="form form-search" action="/search" method="post">

                        <div>
                            <input class="input" type="text" placeholder="Поиск статьи по имени автора..." name="search" required/>
                        </div>

                    </form> <!-- post -->

                </div> <!-- wapper -->

            </body>
            </html>
        '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)