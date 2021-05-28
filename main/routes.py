from app import app
from app.models import *
from flask import render_template,request,redirect



@app.route('/')
def index():
    posts=Post.query.all()
    portheads=PostHeading.query.all()
    headers=PostHeading01.query.all()
    aboutnames=AboutHeading.query.all()
    skills=SkillBar.query.all()
    services=ServicesHeading.query.all()
    serviceboxs=ServicesBox.query.all()
    descs= Experience.query.all()
    feeds=FeedbackHeading.query.all()
    tests=Feedback.query.all()
    icons=SocicalIcon.query.all()
    blogs=Postjs.query.all()
    contacts=ContactHeading.query.all()
    return render_template('main/index.html',posts=posts,portheads=portheads,headers=headers, aboutnames=aboutnames,skills=skills, services=services,serviceboxs=serviceboxs,descs=descs, feeds=feeds,tests=tests,icons=icons,blogs=blogs,contacts=contacts)


