from wtforms import Form, BooleanField, StringField, PasswordField, validators,ValidationError
from flask_babel import gettext
from ...validation import validate_alph_space,validate_html

class LoginForm(Form):
    email = StringField('Email', [validators.Email(message="Email is not a valid")])
    password = PasswordField('Password', [
        validators.DataRequired(),validators.Length(min=8,message="password must be at least 8 digits")
    ])
class UpdatePassForm(Form):
    email = StringField('Email')
    password = PasswordField('Password', [
        validators.DataRequired(),validators.Length(min=8,message="password must be at least 8 digits")
    ])
    c_password = PasswordField('Password', [
        validators.DataRequired(),validators.Length(min=8,message="new password must be at least 8 digits")
    ])
    should_login = BooleanField('Terms')

class RegistrationForm(Form):
    def validate_first_name(form,field):
        if validate_alph_space(field.data):
            message=gettext(u"first name should be only characters")
            raise ValidationError(message)

    def validate_last_name(form,field):
        if validate_alph_space(field.data):
            message=gettext(u"last name should be only characters")
            raise ValidationError(message)

    def validate_html_input(form,field):
        if validate_html(field.data):
            message=gettext(u"Special characters are not allowed")
            raise ValidationError(message)

    email = StringField('Email', [validators.Email(message="Email is not a valid")])
    first_name = StringField('First Name', [validators.Length(max=225),validators.DataRequired(message="first name is required"),
                                            validate_first_name]
                    )
    last_name = StringField('Last Name', [validators.Length(max=225),validators.DataRequired("Last name is required"),
                            validate_last_name])
    password = PasswordField('Password', [
        validators.DataRequired(),validators.Length(min=8,message="password must be alleast 8 digits")
    ])
    terms = BooleanField('Terms', [validators.DataRequired("Please accept our terms")])

