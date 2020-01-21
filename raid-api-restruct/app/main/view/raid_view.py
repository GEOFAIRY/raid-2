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
    return raid_controller.getAllRaids()


@app.route('/raids/<raidId>', methods=['GET'])
def getRaid(raidId):
    """endpoint to return a single raids data
	ApiNote:
			GET /raids/:raidId
	Args:
		raidId: The id of the desired raid to be found.
	Returns:
		Raid of entered id in Json format.
	"""
    return raid_controller.getRaidById(raidId)


@app.route('/raids/<id>/phases', methods=['GET'])
def getRaidPhases(raidId):
	"""endpoint to return all phase data of a given raid
	Apinote:
			GET /raids/:raidId/phases
	Args:
		raidId: The id of the desired raid to be found
	Returns:
		Phases of the entered raid id in Json format.
	"""
	return raid_controller.getPhasesByRaidId(raidId)