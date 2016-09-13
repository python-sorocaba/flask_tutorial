from tvseries import app, db

db.app = app
db.create_all()

print("Database created...")

