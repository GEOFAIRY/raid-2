import os

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import logging

auth = HTTPBasicAuth()

# init the rest api
app = Flask(__name__)
CORS(app)

# check the database exists
baseDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'app/resource/database/db.sqlite')
app.config.from_pyfile(os.path.join(baseDir, 'app/resource/config.cfg'), silent=True)

db = SQLAlchemy(app)
ma = Marshmallow(app)

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# init endpoints
from app.main.view import party_view
from app.main.view import game_view
from app.main.view import party_user_view
from app.main.view import phase_view
from app.main.view import raid_view
from app.main.view import user_view
