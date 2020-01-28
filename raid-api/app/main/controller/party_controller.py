from flask import jsonify
from app import app, db, ma
import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from app.main.model.party import *
from app.main.model.party_user import *


def getParty(id, sherpa, capacity):
    """
	Controller method to get a single party with given id.

	Args:
		id: Id of the party to be found.
	"""
    query = Party.query
    if (id != None):
        query = query.filter(Party.id == id)
    if (sherpa != None):
        if sherpa == "true":
            query = query.filter(Party.sherpa == True)
        else:
            query = query.filter(Party.sherpa == False)


    allParties = query.all()

    if capacity is not None:
        for i in allParties:
            if len(i.partyUsers) > capacity:
                allParties.remove(i)

    result = partiesSchema.dump(allParties)
    if len(result) == 0:
        return "Parties not found", 404
    return jsonify(result)

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
    try:
        db.session.commit()
    except exc.OperationalError:
        return "Database error", 500
    return { "partyId": new_party.id }

def joinPartyById(partyId, joinUser, status):
    """method to add a new partyUser to an existing party

    Arguments:
        partyId {Integer} -- the party to join
        joinUser {User} -- the user to create a PartyUser with and add to party
    """
    joiningParty = Party.query.get(id)
    if joiningParty == None:
        return "Party not found", 404

    if len(joiningParty.partyUsers) > 6:
        new_party_user = PartyUser(joiningParty.id, joinUser.id, True, status)
        joiningParty.partyUsers.append(new_party_user)
        try:
            db.session.commit()
        except exc.OperationalError:
            return "Database error", 500
        return { "partyId": joiningParty.id }
    else:
        return "party full", 400



def leavePartyById(partyId, joinUser):
    """method to leave a new partyUser to an existing party

    Arguments:
        partyId {Integer} -- the party to leave
        joinUser {User} -- the user to leave a PartyUser with and leave to party
    """
    leavingParty = Party.query.get(partyId)

    query = PartyUser.query
    query = query.filter(PartyUser.partyId == partyId)
    query = query.filter(PartyUser.userId == joinUser.userId)
    partyUser = query.all()
    result = partyUserSchema.dump(partyUser)

    if leavingParty == None:
        return "Party not found", 404
    try:
        db.session.delete(result)
    except exc.OperationalError:
        return "Database error", 500
    return { "left party with id of ": partyId}

