from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of the user: ")
    submit = SubmitField("Submit")

class DelForm(FlaskForm):
    id = IntegerField("ID of the user to remove: ")
    submit = SubmitField("Submit")