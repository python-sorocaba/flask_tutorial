from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from tvseries import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

db = SQLAlchemy(app)

from tvseries.core import views  # noqa
