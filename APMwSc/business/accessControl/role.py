import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

from flask import Flask, Blueprint, jsonify,request, json
from flask.ext.sqlalchemy import SQLAlchemy
from flask.templating import render_template
import jinja2
from jinja2.loaders import FileSystemLoader
from sqlalchemy.sql.schema import PrimaryKeyConstraint


app = Flask(__name__,template_folder=dir+"/",static_folder=dir+"/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:holahola@localhost/APMwSc'
db = SQLAlchemy(app)

#Modelo para un rol
from sqlalchemy.sql.schema import PrimaryKeyConstraint
class clsRole(db.Model):
    __tablename__ = 'role'
    namerole = db.Column(db.String(50), nullable   = False )

    usuario  = db.relationship('User' , backref='user', lazy='dynamic')
    idrole   = db.Column(db.Integer   , primary_key= True  )

    def __init__(self,idrole,namerole):
        self.idrole   = idrole
        self.namerole = namerole

    def createDb(self):
        db.create_all()
        db.session.commit()


    def addMe(self):
        db.session.add(self)
        db.session.commit()

    def repr(self):
        print(self.namerole)
        print(self.iddpt)


roleBlueprint = Blueprint('role',__name__,template_folder=dir+"/presentation/access-control/")

@roleBlueprint.route("/role",  methods=['POST','GET'])
def user():
    if request.method == "GET":
        db.create_all()
        db.session.commit()
        return render_template("role.html")
    elif request.method == "POST":
        params  = request.get_json()
        oRole = clsRole(params['idRol'],params['nombreRol'])
        oRole.addMe()
        return render_template("role.html")


