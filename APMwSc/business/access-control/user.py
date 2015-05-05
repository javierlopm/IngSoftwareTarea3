from flask import Flask
from model import db
from flask.ext.sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
db = SQLAlchemy(app)


class tbUser(db.Model):
    __tablename__ = 'user'
    fullname = db.column(db.String(50),              unique=False)
    username = db.column(db.String(16),         primary_key=True )
    password = db.column(db.String(16),              unique=False)
    email    = db.column(db.String(30),              unique=True )
    iddpt    = db.column(db.Integer   ,db.ForeignKey('tbdpt.iddpt'))
    idrole   = db.column(db.Integer   ,db.ForeignKey('tbrole.idrole'))
    
    
    def __init__(self,fullname,username,password,email,iddpt,idrole):        
        self.fullname() = fullname
        self.username() = username
        self.password() = password
        self.email() = email
        self.iddpt() = iddpt #departamento
        self.idrole() = idrole #role
    

        
