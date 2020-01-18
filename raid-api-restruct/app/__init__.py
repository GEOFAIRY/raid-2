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

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'app/resource/database/db.sqlite')
app.config.from_pyfile(os.path.join(baseDir, 'app/resource/config.cfg'), silent=True)

db = SQLAlchemy(app)
ma = Marshmallow(app)


import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# init models
from app.main.model.raid import Raid
from app.main.model.phase import Phase
from app.main.model.game import Game
from app.main.model.party import Party
from app.main.model.partyUser import PartyUser
from app.main.model.user import User

#init endpoints
# from app.main.view import raids
# from app.main.view import users
# from app.main.view import parties

