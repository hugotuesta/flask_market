from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '8d709bfd29b35a257e264c14'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
from market import models