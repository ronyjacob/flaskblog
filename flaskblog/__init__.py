from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#In order to create the secret key got to python interpreter 
#import secrets module
#secrets.token_hex(16) where 16 is the size of the token generated

app.config['SECRET_KEY'] = '630d1c28eb087bf81dc2853299d286ab'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes