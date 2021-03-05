from flask import render_template,request,redirect,url_for,flash
from app import app
from flask_login import login_user,logout_user,login_required
from .forms import RegistrationForm,LoginForm


@authentication.route('/register',methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        word = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('authentication.login'))
        title = "New Account"
    return render_template('register.html',title=Register,form=form)
@authentication.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title=Login,form=form)
@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.index"))