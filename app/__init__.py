# import database ucun
# configire etmek app -i
from flask import flask

app=Flask(__name__)
from main.routes import *
from admin.routes import *
