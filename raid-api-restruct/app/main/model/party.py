from app import app, db, ma
from app.main.model import *
import os

from flask import Flask, jsonify, request, g
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import datetime

"""Party information handler"""


class Party(db.Model):
    """
    class for storing party data
    args:
        partyId - Unique party identifier Int()
        sherpa - if the raid is a sherpa raid Bool()
        timeCreated - the time created DateTime()
    """
    partyId = db.Column(db.Integer, primary_key=True)
    sherpa = db.Column(db.Boolean, nullable=False)
    timeCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    game = db.relationship('Game', backref='party', lazy=True)
    partyUser = db.relationship('PartyUser', backref='party', lazy=True)


    def __init__(self, raidId, sherpa):
        self.raidId = raidId
        self.sherpa = sherpa


class PartySchema(ma.Schema):
    """class for parsng party data"""
    class Meta:
        fields = ('partyId', 'sherpa', 'timeCreated')


# init schemas
partySchema = PartySchema()
partiesSchema = PartySchema(many=True)