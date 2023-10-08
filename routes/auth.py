from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .auths.constants import Constants
from .auths.urls import Urls
from .auths.url_name import Url_Name
from .forms.registeration import RegistrationForm,LoginForm,UpdatePassForm
from  ..models.models import User,db
from flask_babel import gettext
from ..settings import config
from flask_login import login_user
from flask_login import login_required, current_user,logout_user


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

    if current_user and current_user.is_authenticated:
        return redirect(url_for('auth.index'))

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

            if config["DEBUG"]:
                print(new_user.id)

            return redirect(url_for('auth.login'))
        except:
            if config["DEBUG"]:
                print("something wrong went")

    else:
        if config["DEBUG"]:
            print(form.errors)
        return render_template(urls.register_url, form=form)

@bp.route('/login', methods=[constants.GET, constants.POST])
def login():
    if current_user and current_user.is_authenticated:
        return redirect(url_for('auth.index'))

    if request.method == constants.GET:
        return render_template(urls.login_url, name=url_names.login,form='')
    if config["DEBUG"]:
        print(request.form)

    form = LoginForm(request.form)

    if request.method == constants.POST and form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            flash(gettext(u"Email is not found"))
            return render_template(urls.login_url, form=form)

        if not check_password_hash(user.password,form.password.data):
            flash(gettext(u"Password is wrong"),category="errors")
            return render_template(urls.login_url, form=form)

        login_user(user, remember=True)
        flash(gettext(u"You are logged in"),category="info")
        return redirect(url_for('auth.index'))

    else:
        if config["DEBUG"]:
            print(form.errors)
        return render_template(urls.login_url, form=form)


@bp.route('/logout', methods=[constants.GET, constants.POST])
@login_required
def logout():
    logout_user()
    return render_template(urls.login_url, name=url_names.logout)

@login_required
@bp.route('/update-password', methods=[constants.GET, constants.POST])
def forgot_password():
    if request.method == constants.GET:
        print(config["DEBUG"])
        return render_template(urls.forgot_url, name=url_names.forgot_password,config=config)
    form = UpdatePassForm(request.form)

    if request.method == constants.POST and form.validate():
        user = current_user

        if not check_password_hash(user.password,form.password.data):
            flash(gettext(u"Old Password is wrong"),category="errors")
            return render_template(urls.forgot_url, form=form)
        user.password = generate_password_hash(form.c_password.data)
        db.session.commit()

        if not form.should_login.data:
            return redirect(url_for('auth.logout'))
        flash(gettext(u"Password is updated"),category="info")
        return redirect(url_for('auth.forgot_password'))

    else:
        if config["DEBUG"]:
            print(form.errors)
        return render_template(urls.forgot_url, form=form,config=config)