import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .constants import Constants
from .urls import Urls
from .url_name import Url_Name
from .forms.registeration import RegistrationForm

constants = Constants()
urls = Urls()
url_names = Url_Name()

bp = Blueprint("auth", __name__)

@bp.route('/', methods=[constants.GET])
def index():
    if request.method == constants.GET:
        return render_template(urls.index_url, name=url_names.index)

@bp.route('/register', methods=[constants.GET, constants.POST])
def register():
    if request.method == constants.GET:
        return render_template(urls.register_url)
    form = RegistrationForm(request.form)
    print(form.validate())
    if request.method == constants.POST and form.validate():
        pass
    else:
        return render_template(urls.register_url, form=form)

@bp.route('/login', methods=[constants.GET, constants.POST])
def login():
    if request.method == constants.GET:
        return render_template(urls.login_url, name=url_names.login)

@bp.route('/logout', methods=[constants.GET, constants.POST])
def logout():
    if request.method == constants.GET:
        return render_template(urls.login_url, name=url_names.logout)


@bp.route('/update-password', methods=[constants.GET, constants.POST])
def forgot_password():
    if request.method == constants.GET:
        return render_template(urls.login_url, name=url_names.forgot_password)