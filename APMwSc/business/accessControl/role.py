import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

from flask import Flask, Blueprint, redirect,request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.templating import render_template
import jinja2
from jinja2.loaders import FileSystemLoader


app = Flask(__name__,template_folder=dir+"/",static_folder=dir+"/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:holahola@localhost/APMwSc'
db = SQLAlchemy(app)


from sqlalchemy.sql.schema import PrimaryKeyConstraint
class clsRole(db.Model):
    __tablename__ = 'role'
    namerole = db.Column(db.String(50), nullable   = False )
    idrole   = db.Column(db.Integer   , primary_key= True  )

    def __init__(self,idrole,namedpt):
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
@roleBlueprint.route("/role")
def user():
    db.create_all()
    db.session.commit()

    return render_template("role.html")