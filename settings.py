from dotenv import load_dotenv
import os
import json

load_dotenv()
environ = os.environ

config = {
    "DEBUG" : environ.get("FLASK_DEBUG") if environ.get("FLASK_DEBUG") == True else False,
    "SECRET_KEY" : environ.get("SECRET_KEY"),
    "DEFAULT_LOCALE" : environ.get("DEFAULT_LOCALE"),
    "AVAILABLE_LOCALE" : json.loads(environ.get("AVAILABLE_LOCALE")),
    "LOGIN_PATH" : environ.get("LOGIN_PATH"),
}