from flask import jsonify

from app import app
from app.main.controller import raid_controller



@app.route('/raids', methods=['GET'])
def getRaids():
    """endpoint to return all raid data
	ApiNote:
			GET /raids
	Returns
		Json list of all current raids.
	"""
    return RaidsController.getAllRaids()


@app.route('/raids/<id>', methods=['GET'])
def getRaid(id):
    """endpoint to return a single raids data
	ApiNote:
			GET /raids/:id
	Args:
		id: The id of the desired raid to be found.
	Returns:
		Raid of entered id in Json format.
	"""
    return RaidsController.getRaidById(id)
