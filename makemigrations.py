from flask import Flask
from dotenv import load_dotenv
import os
from models.models import db
from flask_migrate import Migrate

load_dotenv()
environ = os.environ


app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

migrate = Migrate(app, db)
