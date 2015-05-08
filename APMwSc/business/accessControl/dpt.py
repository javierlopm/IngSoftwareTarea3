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


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:holahola@localhost/APMwSc'

db = SQLAlchemy(app)

class clsDpt(db.Model):
    
    __tablename__ = 'dpt'
    namedpt  = db.Column(db.String(50), nullable   = False   )
    iddpt    = db.Column(db.Integer   , primary_key= True    )
    
    def __init__(self,iddpt,namedpt):
        self.iddpt   = iddpt
        self.namedpt = namedpt
        print("Agregando "+ str(iddpt) + " " + namedpt)

    def createDb(self):
        db.create_all()
        db.session.commit()


    def addMe(self):
        db.session.add(self)
        db.session.commit()

    def repr(self):
        print(self.namedpt)
        print(self.iddpt)

dptBlueprint = Blueprint('dpt',__name__,template_folder=dir+"/presentation/access-control/")
@dptBlueprint.route("/dpt")
def dpt():
    db.create_all()
    db.session.commit()
    oDpt = clsDpt(1,"Lenguaje")
    oDpt.addMe()

    return render_template("dpt.html")
        

    
