from flask import Flask

from tvseries import config
from tvseries.ext import db
from tvseries.core import core_blueprint

print("Problem: Hen and egg (python circular imports)")
app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
app.register_blueprint(core_blueprint, url_prefix='/')
db.init_app(app)
