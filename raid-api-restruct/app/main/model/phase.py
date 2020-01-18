from app import app, db, ma
from app.main.model import *
import os


from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

"""Phase information handler"""

class Phase(db.Model):
    """
    class for storing phase data
    args:
        id - unique identifier Int()
        raidId - the raid id associated with the raid phase Int()
        order - the order in the phases of this phase e.g. 2nd Int()
        name - the raid name Str()
    """
    id = db.Column(db.Integer, primary_key=True)
    raidId = db.Column(db.Integer, db.ForeignKey('Raid.id'))
    order = db.Column(db.Integer)
    name = db.Column(db.String)

    def __init__(self, raidId, order, name):
        self.raidId = raidId
        self.order = order
        self.name = name


class RaidSchema(ma.Schema):
    """class for parsing raid data correctly"""
    class Meta:
        fields = ('id', 'name', 'image')


#init schemas
raidSchema = RaidSchema()
raidsSchema = RaidSchema(many=True)