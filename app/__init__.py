from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm ,LoginForm
from flask_bootstrap import Bootstrap
from config import config_options

#initializing flask extentions
bootstrap=Bootstrap()

def create_app(config_name):
    app=Flask(__name__)

    app.config['SECRET_KEY']='KAROL!#$@2!0%2&1?'
    app.config['sqlalchemy_batabase_URI']=''
    db=SQLAlchemy(app)

    #initializing flask extentions
    bootstrap.init_app(app)
    #registering blueprints
    from .main import main as main_bueprint
    app.register_blueprint(main_bueprint)

    return app