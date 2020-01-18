from app import app, db, ma
from app.main.model import *
import os


from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

"""Raid information handler"""

class Raid(db.Model):
    """
    class for storing raid data
    args:
        id - unique identifier Int()
        name - the raid name Str()
        image - url to raid banner image Str()
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)

    phases = db.relationship('Phase', backref='raid', lazy=True)
    games = db.relationship('Game', backref='raid', lazy=True)

    def __init__(self, name, image):
        self.name = name
        self.image = image


class RaidSchema(ma.Schema):
    """class for parsing raid data correctly"""
    class Meta:
        fields = ('id', 'name', 'image')


#init schemas
raidSchema = RaidSchema()
raidsSchema = RaidSchema(many=True)