from flask import Flask
from .routes import auth
from os import environ
from flask import g

app = Flask(__name__)
app.register_blueprint(auth.bp)

def create_app():
    g.debug = environ["FLASK_DEBUG"] if "FLASK_DEBUG" in environ else False
    return app
