from app import app, db, ma
import os


from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy



def getAllRaids():
	"""
	Controller method to get all currently available raids.
	"""
    allRaids = Raids.query.all()
    result = raidsSchema.dump(allRaids)
    return jsonify(result)


def getRaidById(id):
    """
	Controller method to get a single raid with given id.

	Args:
		id: Id of the raid to be found.
	"""
    raid = Raids.query.get(id)
    if raid == None:
        return "raid not found", 404
    return raidSchema.jsonify(raid)
