
from flask import Blueprint,render_template,request, flash,redirect,url_for
from .models import User
from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username= username).first()
        if user:
            if check_password_hash(user.password, password):
                
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                    flash('Incorrect password. ',category= 'error')
        else:
            flash('', category='dont-exists')
  


    return render_template("login.html",user=current_user)

@auth.route('/Register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(username= username).first()
        if user:
            flash('Username already exist.', category='error')
        elif len(username)<6:
            flash('username must be greater 6 characters.',category='error')
        elif password1 != password2:
            flash('password don\'t match.',category='error')
        elif len(password1) <8:
            flash('password must be greater 8 characters.',category='error')
        else:
            new_user= User(username=username,first_name= first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('account created.', category='true')
            
            return redirect(url_for('views.home'))
    return render_template("Register.html",user= current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

