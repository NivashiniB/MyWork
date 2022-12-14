from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from company_blog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Your email has already been registered")

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Username has already taken")


class UpdateUserForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    picture = FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Your email has already been registered")

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Username has already taken")

    
