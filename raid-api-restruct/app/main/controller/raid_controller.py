from app import app, db, ma
import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.main.model.raid import *


def getAllRaids():
	"""
	Controller method to get all currently available raids.
	"""
    allRaids = Raid.query.all()
    result = raidsSchema.dump(allRaids)
    return jsonify(result)


def getRaidById(id):
    """
	Controller method to get a single raid with given id.

	Args:
		id: Id of the raid to be found.
	"""
    raidSearched = Raids.query.get(id)
    if raidSearched == None:
        return "raid not found", 404
    return raidSchema.jsonify(raidSearched)
