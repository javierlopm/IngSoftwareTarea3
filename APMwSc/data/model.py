import os
import sys
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
sys.path.append(dir)
dirB = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../business'))
sys.path.append(dirB)

from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.templating import render_template
import jinja2
from jinja2.loaders import FileSystemLoader
from business.accessControl.user import userBlueprint,clsUser
from business.accessControl.role import roleBlueprint
from business.accessControl.dpt import dptBlueprint
from business.accessControl.login import loginBlueprint

app = Flask(__name__,template_folder=dir+"/",static_folder=dir+"/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dsdad:team@localhost/APMwSc'


app.register_blueprint(userBlueprint)
app.register_blueprint(roleBlueprint)
app.register_blueprint(dptBlueprint)
app.register_blueprint(loginBlueprint)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route('/help', methods = ['GET'])
def help():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)


    
db = SQLAlchemy(app)

class User:
     def __init__(self,fullname,username,password,email,iddpt,idrole):
            self.fullname = fullname
            self.username = username
            self.password = password
            self.email    = email
            self.iddpt    = iddpt
            self.idrole   = idrole
class Dpt:
     def __init__(self,iddpt,namedpt):
            self.iddpt    = iddpt
            self.namedpt  = namedpt
class Rol:
     def __init__(self,idrole,namerole):
            self.idrole     = idrole
            self.namerole   = namerole
            
if __name__ == "__main__":
    app.run(debug=True)
