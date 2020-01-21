from flask import jsonify

from app import app
from app.main.controller import party_user_controller


@app.route('/party', methods=['POST'])
def createParty(request):
    """
    endpoint to create a new party from a submitted json request
    required input:
    {
        "sherpa": sherpa
    }
	ApiNote:
		POST /party
    """
    return party_controller.createParty(request)

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