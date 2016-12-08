from flask_wtf import FlaskForm
from wtforms import StringField, DateField


class TVSerieForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    episodies_number = StringField('episodies_number')
    author = StringField('author')
    year = DateField('year')
