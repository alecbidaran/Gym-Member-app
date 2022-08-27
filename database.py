from flask import Flask,jsonify,request,session,render_template,g,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin,login_user,login_required,current_user,logout_user,fresh_login_required
from urllib.parse import urlparse,urljoin
server = Flask(__name__)
server.config['SECRET_KEY']='thisissecret'
server.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Gym_members.db'
server.config['USE_SESSION_FOR_NEXT']=True
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(server)

class Members(db.Model):
    id=db.Column(db.INTEGER,primary_key=True)
    Fullname=db.Column(db.String,unique=True)
    email=db.Column(db.String)
    password=db.Column(db.String)
    sessions=db.Column(db.INTEGER)
    date=db.Column(db.DateTime)



