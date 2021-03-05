from flask import render_template
from . import authentication
from flask_login import login_required

@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def User(id):