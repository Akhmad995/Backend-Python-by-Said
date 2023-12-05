from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm():
    title = StringField('Name', validators=[DataRequired()])
    text = TextAreaField('text', validators=[DataRequired()])
    author = TextAreaField('author', validators=[DataRequired()])
    submit = SubmitField('Submit')