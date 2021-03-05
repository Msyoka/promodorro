from flask import  Flask
from flask_bootstrap import Bootstrap

app=Flask(__name__)

app.config['SECRET_KEY']="karol"
#initializing flask extension
bootstrap=Bootstrap(app)
from app import views