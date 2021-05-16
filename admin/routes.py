from app import app
from app.models import Post
from app import db
from flask import render_template,request,redirect
import os

@app.route('/admin')
def admin_index():
    return  render_template('admin/index.html')


@app.route('/admin/post', methods=['GET','POST']) 
def admin_post():
    posts=Post.query.all()
    if request.method=='POST':
       file=request.files['portfolio_img_url']
       filename=file.filename
       file.save(os.path.join ('app/static/uploads/',filename) )


       post=Post(
          portfolio_name=request.form['portfolio_name'],
          portfolio_header_title=request.form['portfolio_header_title'],
          portfolio_category_name=request.form['portfolio_category_name'],
          portfolio_add_date=request.form['portfolio_add_date'],
          portfolio_img_url=filename
       )     

       db.session.add(post)
       db.session.commit()
       return redirect('/admin/post')
    return render_template('admin/post.html',posts=posts)

