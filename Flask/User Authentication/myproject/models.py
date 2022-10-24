
from sqlalchemy import LABEL_STYLE_TABLENAME_PLUS_COL
from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique = True, index = True)
    user_name = db.Column(db.String(64), unique=True, index = True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    dob = db.Column(db.String(64))
    contact = db.Column(db.String(128)) 
    password_hash = db.Column(db.String(128))

    def __init__(self, email, user_name, password,first_name,last_name,dob,contact):
        self.email = email
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.contact = contact
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
