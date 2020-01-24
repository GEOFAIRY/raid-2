from flask import jsonify

from app import app
from app.main.controller import party_user_controller


@app.route('/party/User', methods=['POST'])
def addPartyUser(request):
    """
    endpoint to add a new user party from a submitted json request
    required input:
    {
        "partyId": partyId
        "userId": userId
        "status": status
		"leader": leader
    }
	ApiNote:
		POST /party/User
    """
    return party_user_controller.addPartyUser(request)