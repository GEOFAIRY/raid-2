from flask import jsonify
from app import app, db, ma
import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.main.model.party import *



def getPartyById(id):
    """
	Controller method to get a single party with given id.

	Args:
		id: Id of the party to be found.
	"""
    partySearched = Party.query.get(id)
    if partySearched == None:
        return "Party not found", 404
    return partySchema.jsonify(partySearched)

def createParty(request):
    """
    method to add a new party from a submitted json request
    required input:
    {
        "sherpa": sherpa
    }
    """
    sherpa = request.json['sherpa']

    new_party = Party(sherpa)