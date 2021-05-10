# model class
from app import db
class Post (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(50))
    user_adress=db.Column(db.String(50))
    user_email=db.Column(db.String(50))
    user_phone=db.Column(db.String(50))
    user_message=db.Column(db.String(50))
    resume_link=db.Column(db.String(50))
    google_map=db.Column(db.String(50))


