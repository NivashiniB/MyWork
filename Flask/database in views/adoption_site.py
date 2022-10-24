import os
from flask import Flask,render_template,redirect,url_for
from forms import AddForm,DelForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

############################
#### SQL DATABASE ##########

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


#### Models #################
class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"User Name: {self.name}"

##### view function #########

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add_user():
    form = AddForm()
    if form.validate_on_submit():

        name = form.name.data
        
        new_user = User(name)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('list_user'))
    return render_template('add.html',form = form)

@app.route('/list')
def list_user():
    users = User.query.all()
    return render_template('list.html',users= users)

@app.route('/delete',methods=['GET','POST'])
def delete_user():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('list_user'))
    return render_template('delete.html',form = form)

if __name__ == "__main__":
    app.run(debug=True)

