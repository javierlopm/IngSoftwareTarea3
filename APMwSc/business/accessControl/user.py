import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)
sys.path.append('.')
from flask import Flask, Blueprint, redirect,request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.templating import render_template
import jinja2
from jinja2.loaders import FileSystemLoader
from business.accessControl.role import db
from business.accessControl.control import clsAccessControl

#Clase de usuario como base de datos
class clsUser(db.Model):
    __tablename__ = 'user'
    fullname = db.Column(db.String(50),    nullable=False)
    username = db.Column(db.String(16), primary_key=True ) #No deberia ser de 16 sino de 97 que es lo que ocupa la clave encriptada
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


#Redireccion a usuario
@userBlueprint.route("/user",  methods=['POST','GET'])
def user():
    if request.method == "GET":
        db.create_all()
        db.session.commit()
        return render_template("user.html")
    elif request.method == "POST":
        params  = request.get_json()

        #Encriptacion de password y verificacion
        oEncript = clsAccessControl()
        password = oEncript.encript(params['passwordO'])

        #Solo si las claves son iguales, y la clave paso por las verificaciones
        #se agrega ala bd
        if(oEncript.check_password(password,params['passwordT'])):
            oUser = clsUser(
                        params['nombre'],
                        params['username'],
                        params['passwordO'],
                        params['correo'],
                        params['idRol'],
                        params['idDpt'])
            oUser.addMe()
        return render_template("user.html")
