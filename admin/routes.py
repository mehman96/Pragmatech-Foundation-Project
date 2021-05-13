from app import app
from app.models import Post
from app import db
import os

from flask import render_template,redirect,request

# @app.route('/admin')
#  def admin_index():     
#     return render_template('/admin/index.html')

@app.route('/admin',methods=['GET', 'POST']) 
def admin_user_():
    posts=Contact.query.all()
    if request.method=='POST':
        post=Contact(
          user_name=request.form['user_name'],
          user_adress=request.form['user_adress'],
          user_email=request.form['user_email'],
          user_phone=request.form['user_phone'],
          user_message=request.form['user_message'],
          resume_link=request.form['resume_link'],
          google_map=request.form['google_map']
        )

     db.session.add(posts)
     db.session.commit()

      return redirect('/admin')
    return render_template('admin/user.html', posts=posts)
