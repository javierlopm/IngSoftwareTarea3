import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

from flask import Flask, Blueprint, redirect,request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.templating import render_template
import jinja2
from jinja2.loaders import FileSystemLoader
from sqlalchemy.sql.schema import PrimaryKeyConstraint


app = Flask(__name__,template_folder=dir+"/",static_folder=dir+"/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:holahola@localhost/APMwSc'
db = SQLAlchemy(app)

roleBlueprint = Blueprint('role',__name__,template_folder=dir+"/presentation/access-control/")
@roleBlueprint.route("/role")
def role():
    return render_template("role.html")

class clsRole(db.Model):
    __tablename__ = 'role'
    namerole  = db.Column(db.String(50),         nullable=False )
    idrole    = db.Column(db.Integer   ,primary_key= True)
    user_role = db.relationship('user', backref='role', lazy='dynamic')
    
    def __init__(self,idrole,namerole):
        self.idrole = idrole
        self.namerole = namerole
        