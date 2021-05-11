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
    test=Post.query.all()
    if request.method=='POST':
        file==request.files['Adınız']
        file==request.files['Email']
        file==request.files['Əlaqə nömrəsi']
        file==request.files['Mesaj buraxın']
        file==request.files['Ünvan']
        file==request.files['resume_link']
        file==request.files['google_map']
    return render_template('admin/user.html',test=test)
    
    db.session.add(test)
    db.session.commit()
    return redirect('/admin/user')
    return render_template('admin/user.html', test=test)