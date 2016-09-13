from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tvseries.sqlite3'
db = SQLAlchemy(app)

from tvseries.core import views  # noqa
