from app import app
from app.models import *
from app import db
from flask import render_template,request,redirect
import os

@app.route('/admin')
def admin_index():
   posts=Post.query.all()
   portheads=PostHeading.query.all()
   headers=PostHeading01.query.all()
   return render_template('admin/index.html', posts=posts,portheads=portheads,headers=headers)

# about start









# about end


# portfolio start
@app.route('/admin/post', methods=['GET','POST']) 
def admin_post():
   posts=Post.query.all()
   if request.method=='POST':
      file=request.files['project_img']
      filename=file.filename
      file.save(os.path.join ('app/static/uploads/',filename))
      post=Post(
         project_name=request.form['project_name'],
         project_img=filename
      )     
      db.session.add(post)
      db.session.commit()
      return redirect('/admin/post')
   return render_template('admin/post.html',posts=posts)


@app.route("/admin/postdelete/<id>")
def postdelete(id):
   post=Post.query.get(id)
   db.session.delete(post)
   db.session.commit()
   return redirect('/admin/post')

@app.route("/admin/postupdate/<id>" , methods=['GET','POST']) 
def postupdate(id):
   post=Post.query.get(id)
   if request.method=='POST':
      file=request.files['project_img']
      filename=file.filename
      file.save(os.path.join ('app/static/uploads/',filename))
      post.project_name=request.form['project_name']
      post.project_img=filename
      db.session.commit()
      return redirect('/admin/post')
   return render_template('admin/postupdate.html',post=post)

@app.route('/admin/porthead', methods=['GET','POST']) 
def admin_porthead():
   portheads=PostHeading.query.all()
   if request.method=='POST':
      porthead=PostHeading(
         portfolio_subheading=request.form['portfolio_subheading'],
         portfolio_heading=request.form['portfolio_heading']
      )     
      db.session.add(porthead)
      db.session.commit()
      return redirect('/admin/porthead')
   return render_template('admin/porthead.html',portheads=portheads)
   
@app.route("/admin/portupdate/<id>" , methods=['GET','POST'])  
def portupdate(id):
   porthead=PostHeading.query.get(id)
   if request.method=='POST':
      porthead.portfolio_subheading=request.form['portfolio_subheading']
      porthead.portfolio_heading=request.form['portfolio_heading']
      db.session.commit()
      return redirect('/admin/porthead')
   return render_template('admin/portheadupdate.html',porthead=porthead)

@app.route("/admin/portdelete/<id>")
def portdelete(id):
   porthead=PostHeading.query.get(id)
   db.session.delete(porthead)
   db.session.commit()
   return redirect('/admin/porthead')

@app.route('/admin/portmenu', methods=['GET','POST']) 
def admin_portmenu():
   headers=PostHeading01.query.all()
   if request.method=='POST':
      header=PostHeading01(
         portfolio_menu_name=request.form['portfolio_menu_name']
      )     
      db.session.add(header)
      db.session.commit()
      return redirect('/admin/portmenu')
   return render_template('admin/portmenu.html',headers=headers)
   

@app.route("/admin/portmenudelete/<id>")
def portmenudelete(id):
   header=PostHeading01.query.all()
   db.session.delete(header)
   db.session.commit()
   return redirect('/admin/portmenu')

@app.route("/admin/portmenuupdate/<id>" , methods=['GET','POST'])  
def portmenuupdate(id):
   header=PostHeading01.query.get(id)
   if request.method=='POST':
      header.portfolio_menu_name=request.form['portfolio_menu_name'],
      db.session.commit()
      return redirect('/admin/porthead')
   return render_template('admin/portmenuupdate.html',header=header)
# portfolio end