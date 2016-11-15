from flask_script import Manager
from flask_collect import Collect
from flask_migrate import Migrate, MigrateCommand

from tvseries import create_app
from tvseries.ext import db
from tvseries.config import DevelopmentConfig

app = create_app(config=DevelopmentConfig)
manager = Manager(app)

# migrate command
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# collect command
collect = Collect()
collect.init_app(app)


@manager.command
def collect():
    """Collect static from blueprints."""
    return app.extensions['collect'].collect()

if __name__ == "__main__":
    manager.run()
