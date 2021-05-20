from app import db

# portfolio start
# class Post (db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     portfolio_name=db.Column(db.String(50))
#     portfolio_header_title=db.Column(db.String(50))
#     portfolio_category_name=db.Column(db.String(50))
#     portfolio_img_url=db.Column(db.String(50))
#     portfolio_add_date=db.Column(db.String(50))


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



    