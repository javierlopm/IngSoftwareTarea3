from model import dir 
import sys
sys.path.append(dir+"/business/access-control")

from flask import Flask
from user import bp

app = Flask(__name__)
app.register_blueprint(userBlueprint,url_prefix="/user")
