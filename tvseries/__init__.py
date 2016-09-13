from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from tvseries import config

print("Problem: Hen and egg (python circular imports)")
app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

db = SQLAlchemy(app)

from tvseries.core import views  # noqa
