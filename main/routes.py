from app import app
from app.models import *
from flask import render_template,request,redirect



@app.route('/')
def index():
    posts=Post.query.all()
    portheads=PostHeading.query.all()
    headers=PostHeading01.query.all()
    return render_template ('main/index.html',posts=posts,portheads=portheads,headers=headers)
