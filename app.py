from flask import Flask,request
from flask_migrate import Migrate
from .routes import auth
from flask import g
from .models.models import db
from flask_babel import Babel
from .settings import config
from flask_login import LoginManager
from .models.models import User
from .settings import config
import json

login_manager = LoginManager()
app = Flask(__name__)

app.config['SECRET_KEY'] =  config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['BABEL_DEFAULT_LOCALE'] = config["DEFAULT_LOCALE"]

def get_locale():
    lang = request.args.get('lang','en')
    if not lang in config["AVAILABLE_LOCALE"]:
        lang = config["DEFAULT_LOCALE"]
    request.accept_languages.best_match(config["AVAILABLE_LOCALE"])
    return lang

babel = Babel(app,locale_selector=get_locale)

db.init_app(app)
migrate = Migrate(app, db)

login_manager.login_view = config["LOGIN_PATH"]
login_manager.session_protection = "strong"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

login_manager.init_app(app)

# register the route here
app.register_blueprint(auth.bp)

def create_app():
    g.debug = config["DEBUG"]
    return app


