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

 # portfolio end


    