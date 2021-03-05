from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm ,LoginForm
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'authentication.login'

#initializing flask extentions
bootstrap=Bootstrap()


def create_app(config_name):
    app=Flask(__name__)
    
    from .authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint,url_prefix = '/authenticate')
    app.config['SECRET_KEY']='KAROL!#$@2!0%2&1?'
    app.config['sqlalchemy_batabase_URI']=''
    db=SQLAlchemy(app)

    #initializing flask extentions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    #registering blueprints
    from .main import main as main_bueprint
    app.register_blueprint(main_bueprint)

    return app