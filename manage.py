from flask import Flask
from app import create_app
from flask_script import Manager,Server
from app.models import User
app=Flask(__name__)

#Creating app instance
app=create_app('development')
manager=Manager(app)
manager.add_command('server',Server)

if __name__ =='__main__':
    manage.py(debug=True)