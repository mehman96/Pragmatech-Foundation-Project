from app import app
from app.models import Post
from app import db
import os

from flask import render_template,redirect,request

@app.route('/admin')
def admin_index():
    return render_template('/admin/index.html')

@app.route('/admin/user',methods=['GET', 'POST']) 
def admin_user_info():
    Posts=usr_info.query.all()
    if request.method=='usr_info':

        file==request.files['user-name']
        file==request.files['user-email']
        file==request.files['user-phone']
        file==request.files['user-message']
        file==request.files['user-adress']
        file==request.files['resume-link']
        file==request.files['google-map']
    return render_template('admin/user.html',Posts=usr_info)

  