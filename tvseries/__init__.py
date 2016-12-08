from flask import Flask

from tvseries import config
from tvseries.ext import db, csrf
from tvseries.core import core_blueprint


def create_app(config=config.ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(core_blueprint, url_prefix='/')
    db.init_app(app)
    csrf.init_app(app)
    return app
