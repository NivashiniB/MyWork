from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,DateField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError

from myproject.models import User

class Login_form(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log in')

class Registration_form(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    user_name = StringField('User Name',validators=[DataRequired()])
    first_name = StringField('First Name',validators=[DataRequired()])
    last_name = StringField('Last Name',validators=[DataRequired()])
    dob = DateField("Date of birth",validators=[DataRequired()])
    contact = StringField("Contact number",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(),EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField("Confirm password",validators=[DataRequired()])
    submit = SubmitField("Register")

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Your email has already been registered!')

    def check_username(self,field):
        if User.query.filter_by(user_name = field.data).first():
            raise ValidationError('User name is taken already!')
