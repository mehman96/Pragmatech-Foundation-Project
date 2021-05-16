from app import app
from app.models import Post
from flask import render_template,request,redirect



@app.route('/')
def index():
    posts=Post.query.all()
    return render_template ('main/index.html',posts=posts)
