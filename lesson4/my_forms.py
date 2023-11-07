import os

from flask import Flask
from flask import render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
csrf = CSRFProtect(app)


class Myform(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

    
@app.route("/", methods=['POST', 'GET'])
def index():
    form = Myform()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        print( name, email, password )

        return redirect('/success')

    return render_template("index.html", form=form)

@app.route("/success", methods=['POST', 'GET'])
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run( host='127.0.0.1', port=8000, debug=True )




