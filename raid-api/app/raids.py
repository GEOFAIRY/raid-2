from app import app, db, ma
import os


from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

"""Raid information handler"""

class Raids(db.Model):
    """
    class for storing raid data
    args:
        id - unique identifier Int()
        name - the raid name Str()
        image - url to raid banner image Str()
        phases - list of encounters in raid (excluding first encounters) Str()
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    phases = db.Column(db.String)

    def __init__(self, name, image, phases):
        self.name = name
        self.image = image
        self.phases = phases


class RaidsSchema(ma.Schema):
    """class for parsing raid data correctly"""
    class Meta:
        fields = ('id', 'name', 'image', 'phases')


#init schemas
raidSchema = RaidsSchema()
raidsSchema = RaidsSchema(many=True)


@app.route('/raids', methods=['GET'])
def getRaids():
    """endpoint to return all raid data"""
    allRaids = Raids.query.all()
    result = raidsSchema.dump(allRaids)
    return jsonify(result)


@app.route('/raids/<id>', methods=['GET'])
def getRaid(id):
    """endpoint to return a single raids data"""
    raid = Raids.query.get(id)
    return raidSchema.jsonify(raid)
