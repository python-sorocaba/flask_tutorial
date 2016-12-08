from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

db = SQLAlchemy()
csrf = CsrfProtect()
