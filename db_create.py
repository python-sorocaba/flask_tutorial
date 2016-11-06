from tvseries import create_app
from tvseries.ext import db

app = create_app()

db.app = app
db.create_all()

print("Database created...")

