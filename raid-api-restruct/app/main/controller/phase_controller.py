from flask import jsonify

from app import app
from app.main.model.phase import *

def getPhaseById(id):
    """
	Controller method to get a single phase with given id.

	Args:
		id: Id of the phase to be found.
	"""
    phaseSearched = Phase.query.get(id)
    if phaseSearched == None:
        return "phase not found", 404
    return phaseSchema.jsonify(phaseSearched)