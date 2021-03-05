from flask import render_template
from app import app

#views
@app.route('/')
def index():
    title=Welcome To Promodoro Timer
    return render_template(index.html,title=title)