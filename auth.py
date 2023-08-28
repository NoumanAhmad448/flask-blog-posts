import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .constants import Constants
from .urls import Urls
from .url_name import Url_Name

constants = Constants()
urls = Urls()
url_names = Url_Name()

bp = Blueprint("auth", __name__)

@bp.route('/register', methods=(constants.GET, constants.POST))
def register():
    if request.method == constants.GET:
        return render_template(urls.register_url, name=url_names.register)