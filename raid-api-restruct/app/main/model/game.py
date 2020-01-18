from app import app, db, ma
from app.main.model import *
import os


from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import datetime

"""Game information handler"""

class Game(db.Model):
    """
    class for storing game data
    args:
        id - unique identifier Int()

    """
    id = db.Column(db.Integer, primary_key=True)
    raidId = db.Column(db.Integer, db.ForeignKey('Raid.id'))
    partyId = db.Column(db.Integer, db.ForeignKey('Party.id'))
    currentPhaseId = db.Column(db.Integer, db.ForeignKey('Phase.id'))
    status = db.Column(db.String)
    timeCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    currentPhase = db.relationship('Phase', backref='game', lazy=True)

    def __init__(self, raidId, partyId, currentPhaseId, status):
        self.raidId = raidId
        self.partyId = partyId
        self.currentPhaseId = currentPhaseId
        self.status = status



class GameSchema(ma.Schema):
    """class for parsing game data correctly"""
    class Meta:
        fields = ('id', 'raidId', 'partyId', 'currentPhaseId', 'status', 'timeCreated')


#init schemas
gameSchema = GameSchema()
gamesSchema = GameSchema(many=True)