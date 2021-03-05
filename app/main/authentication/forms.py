from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,Email,EqualTo,Length
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[Required()])
    email=StringField('Email',validators=[Required(),Email()])
    password=PasswordField('password',validators=Required())
    confirm password=PasswordField('confirm password',validators=[Required(),Equal To('password')])
    submit=SubmitField('Sign up')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginFormForm(FlaskForm):
    email=StringField('Email',validators=[Required(),Email()])
    password=PasswordField('password',validators=Required())
    remember=BooleanField('Remember me')
    submit=SubmitField('Login')
class SettimerForm(FlaskForm):
    WorkingHours=StringField('Work duration',validators=[Required, Length(min=1,max=3)])
    breaktime=StringField('Break duration' validators=[Required, Length(min=5,max=9)])
    activity=TextAreaField('Break Activity' validators=[Required])
def validate_email(self,data_field):
    if User.query.filter_by(email =data_field.data).first():
        raise ValidationError('There is an account with that email')

def validate_username(self,data_field):
    if User.query.filter_by(username = data_field.data).first():
        raise ValidationError('That username is taken')
               
    
