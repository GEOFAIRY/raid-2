from flask import Flask, jsonify, request, g

from app import app, auth
from app.main.controller import party_controller


@app.route('/party', methods=['POST'])
@auth.login_required
def createParty():
    """
    endpoint to create a new party from a submitted json request
    required input:
    {
        "sherpa": sherpa
    }
	ApiNote:
		POST /party
    """
    creatingUser = g.user
    if request.json['sherpa'] == "True":
        sherpa = True
    else:
        sherpa = False
    status = "Not Ready"

    return party_controller.createParty(creatingUser, sherpa, status)

@app.route('/party', methods=['GET'])
def getParty():
    """endpoint to return a single party data
	ApiNote:
			GET /party/:partyId
	Returns:
		list of parties with searach terms in Json format.
	"""
    id = request.args.get('id', default = None, type = int)
    sherpa = request.args.get('sherpa', default = None, type = str)
    capacity = request.args.get('capacity', default = None, type = int)

    return party_controller.getParty(id, sherpa, capacity)

@app.route('/party/<partyId>/join', methods=['PATCH'])
@auth.login_required
def joinParty(partyId):
    joinUser = g.user
    status = "Not Ready"
    return party_controller.joinPartyById(partyId, joinUser, status)


@app.route('/party/<partyId>/leave', methods=['PATCH'])
@auth.login_required
def leaveParty(partyId):
    joinUser = g.user
    return party_controller.leavePartyById(partyId, joinUser)