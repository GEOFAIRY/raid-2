from app import app, db, ma
import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.main.model.raid import *
from app.main.model.phase import phasesSchema


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


def getPhasesByRaidId(raidId):
    """
	Controller method to get a single raids phases with a given id.

	Args:
		raidId: Id of the raid phases to be found
	"""
    raidSearched = Raids.query.get(raidId)
    if raidSearched = None:
        return "raid not found", 404
    result = phasesSchema.dump(raidSearched.phases)
    return jsonify(result)