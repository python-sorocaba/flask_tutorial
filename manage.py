from flask_script import Manager
from tvseries import create_app
from tvseries.config import DevelopmentConfig

app = create_app(config=DevelopmentConfig)
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
