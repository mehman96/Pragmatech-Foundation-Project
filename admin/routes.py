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
   return render_template('admin/index.html', posts=posts,portheads=portheads,headers=headers,aboutnames=aboutnames,skills=skills,services=services,serviceboxs=serviceboxs,descs=descs, feeds= feeds,tests=tests,icons=icons,blogs=blogs,contacts=contacts)

# about start
@app.route('/admin/aboutname', methods=['GET','POST']) 
def adminAbout():
   aboutnames=AboutHeading.query.all()
   if request.method=='POST':
      aboutname=AboutHeading(
         about_desc_name=request.form['about_desc_name'],
         about_heading_name=request.form['about_heading_name']
      )     
      db.session.add(aboutname)
      db.session.commit()
      return redirect('/admin/aboutname')
   return render_template('admin/aboutname.html',aboutnames=aboutnames)
   
@app.route("/admin/aboutdelete/<id>")
def aboutdelete(id):
   aboutname=AboutHeading.query.get(id)
   db.session.delete(aboutname)
   db.session.commit()
   return redirect('/admin/aboutname')


@app.route("/admin/aboutupdate/<id>" , methods=['GET','POST'])  
def aboutupdate(id):
   aboutname=AboutHeading.query.get(id)
   if request.method=='POST':
      aboutname.about_heading_name=request.form['about_heading_name']
      aboutname.about_desc_name=request.form['about_desc_name']
      db.session.commit()
      return redirect('/admin/aboutname')
   return render_template('admin/aboutupdate.html',aboutname=aboutname)

# about end

# skill-bar start  
# add
@app.route('/admin/skill', methods=['GET','POST']) 
def SkillAbout():
   skills=SkillBar.query.all()
   if request.method=='POST':
      skill=SkillBar(
      skill_name=request.form['skill_name'],
      skill_persantage=request.form['skill_persantage']
      )     
      db.session.add(skill)
      db.session.commit()
      return redirect('/admin/skill')
   return render_template('admin/skill.html',skills=skills)
   #

   # delete
@app.route("/admin/skilldelete/<id>")
def skilldelete(id):
   skill=SkillBar.query.get(id)
   db.session.delete(skill)
   db.session.commit()
   return redirect('/admin/skill')
 
   #

# update

@app.route("/admin/skillupdate/<id>" , methods=['GET','POST'])  
def Skillupdate(id):
   skill=SkillBar.query.get(id)
   if request.method=='POST':
      skill.skill_name=request.form['skill_name']
      skill.skill_persantage=request.form['skill_persantage']
      db.session.commit()
      return redirect('/admin/skill')
   return render_template('admin/skillupdate.html',skill=skill)

# 

# skill-bar end


# servies start 

# add
@app.route('/admin/serviceshead', methods=['GET','POST']) 
def ServicesHead():
   services=ServicesHeading.query.all()
   if request.method=='POST':
      services=ServicesHeading(
      services_subheading=request.form['services_subheading'],
      services_heading=request.form['services_heading']
      )     
      db.session.add(services)
      db.session.commit()
      return redirect('/admin/serviceshead')
   return render_template('admin/serviceshead.html',services=services)

# 

# delete
@app.route("/admin/servicesheaddelete/<id>")
def Servicesdelete(id):
   service=ServicesHeading.query.get(id)
   db.session.delete(service)
   db.session.commit()
   return redirect('/admin/serviceshead')
 
# 

# update
@app.route("/admin/servicesheadupdate/<id>" , methods=['GET','POST'])  
def Servicesupdate(id):
   service=ServicesHeading.query.get(id)
   if request.method=='POST':
      service.services_subheading=request.form['services_subheading']
      service.services_heading=request.form['services_heading']
      db.session.commit()
      return redirect('/admin/serviceshead')
   return render_template('admin/servicesheadupdate.html',service=service)

# 

# services box
# add
@app.route('/admin/servicesbox', methods=['GET','POST']) 
def servicesbox():
   serviceboxs=ServicesBox.query.all()
   if request.method=='POST':
      servicebox=ServicesBox(
         services_icon=request.form['services_icon'],
         services_title_heading=request.form['services_title_heading'],
         services_title=request.form['services_title']
      )     
      db.session.add(servicebox)
      db.session.commit()
      return redirect('/admin/servicesbox')
   return render_template('admin/servicesbox.html',serviceboxs=serviceboxs)

# 

# delete
@app.route("/admin/servicesboxdelete/<id>")
def Servicesboxdelete(id):
   servicebox=ServicesBox.query.get(id)
   db.session.delete(servicebox)
   db.session.commit()
   return redirect('/admin/servicesbox')
 
# 

# update
@app.route("/admin/servicesboxupdate/<id>" , methods=['GET','POST'])  
def Servicesboxupdate(id):
   servicebox=ServicesBox.query.get(id)
   if request.method=='POST':
         servicebox.services_icon=request.form['services_icon']
         servicebox.services_title_heading=request.form['services_title_heading']
         servicebox.services_title=request.form['services_title']
         db.session.commit()
         return redirect('/admin/servicesbox')
   return render_template('admin/servicesboxupdate.html',servicebox=servicebox)

# 

# services end

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
         project_header=request.form['project_header'],
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
      post.project_header=request.form['project_header']
      post.project_img=filename
      db.session.commit()
      return redirect('/admin/post')
   return render_template('admin/postupdate.html',post=post)

# post js start 
# add
@app.route('/admin/blog', methods=['GET','POST']) 
def blog():
   blogs=Postjs.query.all()
   if request.method=='POST':
      file=request.files['project_close_img']
      file=request.files['project_img_js']
      filename=file.filename
      file.save(os.path.join ('app/static/uploads/',filename))
      blog=Postjs(
         project_name_js=request.form['project_name_js'],
         project_header_js =request.form['project_header_js'],
         project_desc_js=request.form['project_desc_js'],  
         project_client=request.form['project_client'],
         project_cat=request.form['project_cat'],
         project_cat_name =request.form['project_cat_name'],
         project_client_name=request.form['project_client_name'],
         close_icon=request.form['close_icon'],
         close_icon_name=request.form['close_icon_name'],
         project_close_img=filename,
         project_img_js=filename
      )     
      db.session.add(blog)
      db.session.commit()
      return redirect('/admin/blog')
   return render_template('admin/blog.html',blogs=blogs)


# delete

@app.route("/admin/blogdelete/<id>")
def blogdelete(id):
   blog=Postjs.query.get(id)
   db.session.delete(blog)
   db.session.commit()
   return redirect('/admin/blog')

# update


@app.route("/admin/blogupdate/<id>" , methods=['GET','POST']) 
def blogupdate(id):
   blog=Postjs.query.get(id)
   if request.method=='POST':
      file=request.files['project_close_img']
      file=request.files['project_img_js']
      filename=file.filename
      file.save(os.path.join('app/static/uploads/',filename))
      blog.project_name_js=request.form['project_name_js']
      blog.project_header_js =request.form['project_header_js']
      blog.project_desc_js=request.form['project_desc_js']  
      blog.project_client=request.form['project_client']
      blog.project_cat=request.form['project_cat']
      blog.project_cat_name =request.form['project_cat_name']
      blog.project_client_name=request.form['project_client_name']
      blog.close_icon=request.form['close_icon']
      blog.close_icon_name=request.form['close_icon_name']
      blog.project_close_img=filename
      blog.project_img_js=filename
      db.session.commit()
      return redirect('/admin/blog')
   return render_template('admin/blogupdate.html',blog=blog)











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
   header=PostHeading01.query.get(id)
   db.session.delete(header)
   db.session.commit()
   return redirect('/admin/portmenu')

@app.route("/admin/portmenuupdate/<id>" , methods=['GET','POST'])  
def portmenuupdate(id):
   header=PostHeading01.query.get(id)
   if request.method=='POST':
      header.portfolio_menu_name=request.form['portfolio_menu_name']
      db.session.commit()
      return redirect('/admin/porthead')
   return render_template('admin/portmenuupdate.html',header=header)










# portfolio end

# education start
# add
@app.route('/admin/experience', methods=['GET','POST']) 
def experince():
   descs= Experience.query.all()
   if request.method=='POST':
      desc=Experience(
         start_date=request.form['start_date'],
         end_date=request.form['end_date'],
         title_header=request.form['title_header'],
         desc=request.form['desc']
      )     
      db.session.add(desc)
      db.session.commit()
      return redirect('/admin/experience')
   return render_template('admin/experience.html',descs=descs)

# 

# delete
@app.route("/admin/experincedelete/<id>")
def Experincedelete(id):
   desc= Experience.query.get(id)
   db.session.delete(desc)
   db.session.commit()
   return redirect('/admin/experience')
 
# 

# update
@app.route("/admin/experienceupdate/<id>" , methods=['GET','POST'])  
def Experinceupdate(id):
   desc= Experience.query.get(id)
   if request.method=='POST':
         desc.start_date=request.form['start_date']
         desc.end_date=request.form['end_date']
         desc.title_header=request.form['title_header']
         desc.desc=request.form['desc']

         db.session.commit()
         return redirect('/admin/experience')
   return render_template('admin/experienceupdate.html',desc=desc)

# 


# education end


# testimionals start
# add
@app.route('/admin/feedbackheading', methods=['GET','POST']) 
def feedbackheading():
   feeds=FeedbackHeading.query.all()
   if request.method=='POST':
      feed=FeedbackHeading(
         testi_subheading=request.form['testi_subheading'],
         testi_heading=request.form['testi_heading']
      
      )     
      db.session.add(feed)
      db.session.commit()
      return redirect('/admin/feedbackheading')
   return render_template('admin/feedbackheading.html',feeds=feeds)

# 


# delete
@app.route("/admin/feedbackheadingdelete/<id>")
def fedbackheadindelete(id):
   feed=FeedbackHeading.query.get(id)
   db.session.delete(feed)
   db.session.commit()
   return redirect('/admin/feedbackheading')
 
# 

@app.route("/admin/feedbackheadingupdate/<id>" , methods=['GET','POST'])  
def feedbackheadingupdate(id):
   feed=FeedbackHeading.query.get(id)
   if request.method=='POST':
         feed.testi_subheading=request.form['testi_subheading']
         feed.testi_heading=request.form['testi_heading']
         db.session.commit()
         return redirect('/admin/feedbackheading')
   return render_template('admin/feedbackheadingupdate.html',feed=feed)
# 

# Feedback start
# add
@app.route('/admin/feedback', methods=['GET','POST']) 
def feedback():
   tests=Feedback.query.all()
   if request.method=='POST':
      file=request.files['commenter_img']
      filename=file.filename
      file.save(os.path.join ('app/static/uploads/',filename))
      test=Feedback(
         commenter_name=request.form['commenter_name'],
         commenter_title=request.form['commenter_title'],
         commenter_social_media=request.form['commenter_social_media'],
         commenter_desc=request.form['commenter_desc'],
         commenter_img=filename

      )     
      db.session.add(test)
      db.session.commit()
      return redirect('/admin/feedback')
   return render_template('admin/feedback.html',tests=tests)

#delete 

@app.route("/admin/feedbackdelete/<id>")
def feedbackdelete(id):
   test=Feedback.query.get(id)
   db.session.delete(test)
   db.session.commit()
   return redirect('/admin/feedback')

# 

# update

@app.route("/admin/feedbackupdate/<id>" , methods=['GET','POST']) 
def feedbackupdate(id):
   test=Feedback.query.get(id)
   if request.method=='POST':
      file=request.files['commenter_img']
      filename=file.filename
      file.save(os.path.join ('app/static/uploads/',filename))
      test.commenter_name=request.form['commenter_name']
      test.commenter_title=request.form['commenter_title']
      test.commenter_social_media=request.form['commenter_social_media']
      test.commenter_desc=request.form['commenter_desc']
      test.commenter_img=filename
      db.session.commit()
      return redirect('/admin/test')
   return render_template('admin/feedbackupdate.html',test=test)

# 



# Feedback end


# testimionals end





# contact start

# contact heading 
# add

@app.route('/admin/contactheading', methods=['GET','POST']) 
def contactheading():
   contacts=ContactHeading.query.all()
   if request.method=='POST':
      contact=ContactHeading(
      contact_subheading_name =request.form['contact_subheading_name'],
      contact_heading_name=request.form['contact_heading_name']
      )     
      db.session.add(contact)
      db.session.commit()
      return redirect('/admin/contact')
   return render_template('admin/contactheading.html',contacts=contacts)
   
   # update
@app.route("/admin/contactheadingupdate/<id>" , methods=['GET','POST'])  
def contactupdate(id):
   contact=ContactHeading.query.get(id)
   if request.method=='POST':
      contact.contact_subheading_name=request.form['contact_subheading_name']
      contact.contact_heading_name=request.form['contact_heading_name']
      db.session.commit()
      return redirect('/admin/contact')
   return render_template('admin/contactheading.html',contact=contact)

@app.route("/admin/contactheadingdelete/<id>")
def contactdelete(id):
   contact=ContactHeading.query.get(id)
   db.session.delete(contact)
   db.session.commit()
   return redirect('/admin/contact')





# contact end


# social-icon start
@app.route('/admin/social', methods=['GET','POST']) 
def socicalIcon():
   icons= SocicalIcon.query.all()
   if request.method=='POST':
      icon=SocicalIcon(
      social_icon_name=request.form['social_icon_name'],
      social_icon=request.form['social_icon'],
      social_icon_link=request.form['social_icon_link']
      )     
      db.session.add(icon)
      db.session.commit()
      return redirect('/admin/social')
   return render_template('admin/social.html',icons=icons)


# delete
@app.route("/admin/socialdelete/<id>")
def socialdelete(id):
   icon = SocicalIcon.query.get(id)
   db.session.delete(icon)
   db.session.commit()
   return redirect('/admin/social')
 
# 

# update
@app.route("/admin/socialupdate/<id>" , methods=['GET','POST'])  
def socialupdate(id):
   icon = SocicalIcon.query.get(id)
   if request.method=='POST':
         icon.social_icon_name=request.form['social_icon_name']
         icon.social_icon=request.form['social_icon']
         icon.social_icon_link=request.form['social_icon_link']
         db.session.commit()
         return redirect('/admin/social')
   return render_template('admin/socialupdate.html',icon=icon)

# 






# social-icon end








