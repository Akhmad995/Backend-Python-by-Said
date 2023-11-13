import os
import sqlite3

from flask import Flask
from flask import render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect


from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
csrf  = CSRFProtect(app)

class Myform(FlaskForm):
    title = StringField( 'Post title', validators=[ DataRequired(),  Length( max = 10, message = "Слишком много символов" ) ] )
    text = TextAreaField( 'Post text', validators=[ DataRequired() ] )
    name = StringField( 'Name author', validators=[ DataRequired() ] )
    email = EmailField( 'Email author', validators=[ DataRequired() ] )
    date = DateField( 'Post date', validators=[ DataRequired() ] )
    submit = SubmitField( 'Submit')
    

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    form = Myform()

    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        name = form.name.data
        email = form.email.data
        date = form.date.data

        print( title, text, name, email, date)

        return redirect("/success")
    return render_template("admin.html", form=form)

        
@app.route('/success')
def seccess():
    return render_template("success.html")


if __name__ == '__main__':
    app.run( host='127.0.0.1', port=8000, debug=True )

