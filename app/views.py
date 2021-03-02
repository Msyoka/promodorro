from flask import render_template,request,redirect,url_for,flash
from app import app
from .form import RegistrationForm,LoginForm


@app.route('/register')
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('login'))
    return render_template('register.html',title=Register,form=form)
@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title=Login,form=form)