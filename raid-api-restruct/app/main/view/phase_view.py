from flask import jsonify

from app import app
from app.main.model import phase
from app.main.controller import phase_controller


@app.route('/phase', methods=['POST'])
def createPhase(request):
    """
    endpoint to create a new phase from a submitted json request
    required input:
    {
        "raidId": raidId
		"order": order
		"name": name
    }
	ApiNote:
		POST /phase
    """
    return phase_controller.createPhase(request)

@app.route('/phase/<id>', methods=['GET'])
def getPhase(id):
    """endpoint to return a single phase data
	ApiNote:
			GET /phase/:id
	Args:
		id: The id of the desired phase to be found.
	Returns:
		phase of entered id in Json format.
	"""
    return phase_controller.getPhaseById(id)