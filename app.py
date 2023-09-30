from flask import Flask
from dotenv import load_dotenv
import os
from .routes import auth
from flask import g

load_dotenv()
environ = os.environ

app = Flask(__name__)
app.register_blueprint(auth.bp)

def create_app():
    g.debug = environ.get("FLASK_DEBUG")
    return app
