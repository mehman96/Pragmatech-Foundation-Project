from app import app
from app.models import Post
from flask import render_template,redirect,request

@app.route('/')
def index():
    test=Post.query.all()
    return render_template('/main/index.html',test=test)

    