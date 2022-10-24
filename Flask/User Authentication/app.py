from myproject import db,app
from flask import redirect,render_template,request,url_for,flash,abort
from flask_login import login_required,login_user,logout_user
from myproject.models import User
from myproject.forms import Login_form,Registration_form

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you have been logged out!")
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Log in successful!")

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('welcome')
            
            return redirect(next)
    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():

    form = Registration_form()

    if form.validate_on_submit():
        user = User(email = form.email.data, user_name= form.user_name.data, password= form.password.data,
                     first_name = form.first_name.data, last_name = form.last_name.data, dob = form.dob.data,
                     contact = form.contact.data)
        
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registering!")
        return redirect(url_for('login'))

    return render_template('register.html',form=form)

if __name__ =='__main__':
    app.run(debug=True)   
            
