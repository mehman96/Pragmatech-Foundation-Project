# import database paccage
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db' 
db=SQLAlchemy(app)
from app.models import*
from main.routes import*
from admin.routes import*

# db.create_all()