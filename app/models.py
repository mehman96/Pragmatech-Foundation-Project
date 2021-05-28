from app import db
# about start
class AboutHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    ab_name=db.Column(db.String(50))
    about_desc_name=db.Column(db.String(50))
    about_heading_name=db.Column(db.String(50))

class SkillBar(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skill_name=db.Column(db.String(50))
    skill_persantage=db.Column(db.String(50))

# about end

# my_services  start
class ServicesHeading(db.Model):
        id=db.Column(db.Integer,primary_key=True)
        services_subheading=db.Column(db.String(50))
        services_heading=db.Column(db.String(50))
        

class ServicesBox(db.Model):
        id=db.Column(db.Integer,primary_key=True)
        services_icon=db.Column(db.String(50))
        services_title_heading=db.Column(db.String(50))
        services_title=db.Column(db.String(50))

# my_services end


# portfolio start

class PostHeading (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    portfolio_subheading=db.Column(db.String(50))
    portfolio_heading=db.Column(db.String(50))
    
class PostHeading01(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    portfolio_menu_name=db.Column(db.String(50))

class Post (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_name=db.Column(db.String(50))
    project_img=db.Column(db.String(50))
    project_header=db.Column(db.String(50))


class Postjs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_close_img=db.Column(db.String)
    project_name_js=db.Column(db.String)
    project_header_js=db.Column(db.String)
    project_img_js=db.Column(db.String)
    project_desc_js=db.Column(db.String)
    project_client=db.Column(db.String)
    project_cat=db.Column(db.String)
    project_cat_name=db.Column(db.String)
    project_client_name=db.Column(db.String)
    close_icon=db.Column(db.String)
    close_icon_name=db.Column(db.String)

    


























 # portfolio end














# portfolio end
    

# education start

class Experience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    start_date=db.Column(db.String(50))
    end_date=db.Column(db.String(50))
    title_header=db.Column(db.String(50))
    desc=db.Column(db.String(50))

class Education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    edu_start_date=db.Column(db.String(50))
    edu_end_date=db.Column(db.String(50))
    edu_title_header=db.Column(db.String(50))
    edu_desc=db.Column(db.String(50))

# education end


# testimionals start

class FeedbackHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    testi_subheading=db.Column(db.String(50))
    testi_heading=db.Column(db.String(50))


class Feedback (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    commenter_img =db.Column(db.String(50))
    commenter_name=db.Column(db.String(50))
    commenter_title=db.Column(db.String(50))
    commenter_social_media=db.Column(db.String(50))
    commenter_desc=db.Column(db.String(50))

   
# testimionals end


# contact start 

class ContactHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_subheading_name=db.Column(db.String(50))
    contact_heading_name=db.Column(db.String(50))


class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_icon=db.Column(db.String(50))
    contact_desc=db.Column(db.String(50))
    contact_link=db.Column(db.String(50))


class ContactMe(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(50))
    user_email=db.Column(db.String(50))
    user_phone=db.Column(db.String(50))
    user_message=db.Column(db.Text)

# contact end


# social-icon start
class SocicalIcon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    social_icon_name=db.Column(db.String(50))
    social_icon=db.Column(db.String(50))
    social_icon_link=db.Column(db.String(50))
# social-icon end





