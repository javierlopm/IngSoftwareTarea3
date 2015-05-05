from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import psycopg2
from flask.templating import render_template
import os
import jinja2
from jinja2.loaders import FileSystemLoader

dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..'))
app = Flask(__name__,template_folder=dir+"/",static_folder=dir+"/static")

print(dir+"/static")

app.secret_key = "justALamePass"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dsdad:team@localhost/APMwSc'


print("realpath "+os.path.dirname(os.path.realpath(__file__)))

print(dir+"/")

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/dpt")
def dpt():
    return render_template("/presentation/access-control/dpt.html")

@app.route("/role")
def role():
    return render_template("/presentation/access-control/role.html")

@app.route("/login")
def login():
    return render_template("/presentation/access-control/login.html")

@app.route("/user")
def user():
    return render_template("/presentation/access-control/user.html")

    
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
