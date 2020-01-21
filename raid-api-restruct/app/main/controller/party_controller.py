from flask import jsonify
from app import app, db, ma
import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from app.main.model.party import *
from app.main.model.party_user import *


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

def createParty(creatingUser, sherpa, status):
    """
    method to add a new party from a submitted json request
    required input:
    {
        "sherpa": sherpa
    }
    """
    new_party = Party(sherpa)
    new_party_user = PartyUser(new_party.id, creatingUser.id, True, status)
    new_party.partyUsers.append(new_party_user)
    db.session.add(new_party)
    # try:
    db.session.commit()
    # except exc.OperationalError:
    #     return "Database error", 500
    return { "partyId": new_party.id }