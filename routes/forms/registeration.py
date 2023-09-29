from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    email = StringField('Email', [validators.Email()])
    first_name = StringField('First Name', [validators.Length(max=225),validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(max=225),validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])
    terms = BooleanField('Terms', [validators.DataRequired()])