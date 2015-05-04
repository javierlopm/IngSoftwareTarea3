from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


class tbUser(db.Model):
    __tablename__ = 'user'
    
    fullname = db.column(db.string(50),              unique=False)
    username = db.column(db.string(16),         primary_key=True )
    password = db.column(db.string(16),              unique=False)
    email    = db.column(db.string(30),              unique=True )
    iddpt    = db.column(db.Integer   ,db.ForeignKey('tbdpt.iddpt'))
    idrole   = db.column(db.Integer   ,db.ForeignKey('tbrole.idrole'))
    
    def __init__(self,fullname,username,password,email,iddpt,idrole):
        self.fullname() = fullname
        self.username() = username
        self.password() = password
        self.email() = email
        self.iddpt() = iddpt #departamento
        self.idrole() = idrole #role
        

    def insert(self):
        