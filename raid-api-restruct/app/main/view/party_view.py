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
    status = "Waiting for Players"

    return party_controller.createParty(creatingUser, sherpa, status)

@app.route('/party/<id>', methods=['GET'])
def getParty(id):
    """endpoint to return a single party data
	ApiNote:
			GET /party/:id
	Args:
		id: The id of the desired party to be found.
	Returns:
		party of entered id in Json format.
	"""
    return party_controller.getPartyById(id)