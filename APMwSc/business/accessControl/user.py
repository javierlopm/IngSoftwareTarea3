import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

from flask import Flask, Blueprint, redirect,request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.templating import render_template
import jinja2
from jinja2.loaders import FileSystemLoader


app = Flask(__name__,template_folder=dir+"/presentation/access-control",static_folder=dir+"/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:holahola@localhost/APMwSc'

userBlueprint = Blueprint('user',__name__,template_folder=dir+"/presentation/access-control/")
db = SQLAlchemy(app)

@userBlueprint.route("/user")
def user():
    return render_template("user.html")

class clsUser(db.Model):
    __tablename__ = 'user'
    fullname = db.Column(db.String(50),              nullable=False)
    username = db.Column(db.String(16),         primary_key=True )
    password = db.Column(db.String(16),              nullable=False)
    email    = db.Column(db.String(30),              unique=True )
    iddpt    = db.Column(db.Integer   ,db.ForeignKey('clsDpt.iddpt'))
    idrole   = db.Column(db.Integer   ,db.ForeignKey('clsRole.idrole'))
    
    
    def __init__(self,fullname,username,password,email,iddpt,idrole):        
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email    = email
        self.iddpt    = iddpt   #departamento
        self.idrole   = idrole #role
    


        
#if __name__ == "__main__":
#    app.run(debug=True)
