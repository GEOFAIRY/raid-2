import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

#init the rest api
app = Flask(__name__)
CORS(app)

#check the database exists
baseDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'db.sqlite')
app.config.from_pyfile(os.path.join(baseDir, 'config.cfg'), silent=True)

db = SQLAlchemy(app)
ma = Marshmallow(app)


import logging

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

#init endpoints
from app import raids
from app import users
from app import parties

