from app import app, db, ma
import os


from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


class Raids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    phases = db.Column(db.String)

    def __init__(self, name, image, phases):
        self.name = name
        self.image = image
        self.phases = phases


class RaidsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'image', 'phases')


raidSchema = RaidsSchema()
raidsSchema = RaidsSchema(many=True)


@app.route('/raids', methods=['GET'])
def getRaids():
    allRaids = Raids.query.all()
    result = raidsSchema.dump(allRaids)
    return jsonify(result)


@app.route('/raids/<id>', methods=['GET'])
def getRaid(id):
    raid = Raids.query.get(id)
    return raidSchema.jsonify(raid)