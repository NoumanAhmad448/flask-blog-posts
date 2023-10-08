from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .auths.constants import Constants
from .auths.urls import Urls
from .auths.url_name import Url_Name
from .forms.registeration import RegistrationForm
from  ..models.models import User,db
from flask_babel import gettext

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
        return render_template(urls.register_url,form='')
    form = RegistrationForm(request.form)

    if request.method == constants.POST and form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            form.errors["email"] = [gettext(u"duplicate email is found")]
            return render_template(urls.register_url, form=form)

        new_user = User(email=form.email.data, first_name=form.first_name.data,last_name=form.last_name.data,
                        password=generate_password_hash(form.password.data, method='sha256'),is_active=1)

        # add the new user to the database
        try:
            db.session.add(new_user)
            db.session.commit()
            print(new_user.id)
            return redirect(url_for('auth.login'))
        except:
            print("something wrong went")

    else:
        print(form.errors)
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