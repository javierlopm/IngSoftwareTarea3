import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

from flask import Flask, Blueprint, redirect,request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.templating import render_template
import jinja2
from jinja2.loaders import FileSystemLoader
from business.accessControl.role import db

app = Flask(__name__,template_folder=dir+"/presentation/access-control",static_folder=dir+"/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:holahola@localhost/APMwSc'

#db = SQLAlchemy(app)



class clsUser(db.Model):
    __tablename__ = 'user'
    fullname = db.Column(db.String(50),    nullable=False)
    username = db.Column(db.String(16), primary_key=True )
    password = db.Column(db.String(16),    nullable=False)
    email    = db.Column(db.String(30),      unique=True )
    iddpt    = db.Column(db.Integer   ,db.ForeignKey('dpt.iddpt'))
    idrole   = db.Column(db.Integer   ,db.ForeignKey('role.idrole'))
    
    
    def __init__(self,fullname,username,password,email,iddpt,idrole):        
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email    = email
        self.iddpt    = iddpt   #departamento
        self.idrole   = idrole  #role

    def repr(self):
        return '<Usuario %r>' % self.fullname
    

userBlueprint = Blueprint('user',__name__,template_folder=dir+"/presentation/access-control/")


@userBlueprint.route("/user",  methods=['POST','GET'])
def user():
    if request.method == "GET":
        db.create_all()
        db.session.commit()
        return render_template("user.html")
    elif request.method == "POST":
        params  = request.get_json()
        print(params)
        oUser = clsUser(params['idDpt'],params['nombreDpt'])
        oUser.addMe()
        return render_template("user.html")
