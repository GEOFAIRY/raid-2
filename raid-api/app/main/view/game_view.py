from flask import jsonify

from app import app
from app.main.controller import raid_controller





@app.route('/game', methods=['GET'])
def getGame():
    """endpoint to return a single games data
        ApiNote:
                        GET /game/:id
        Args:
                id: The id of the desired game to be found.
        Returns:
                game of entered id in Json format.
        """

    id = request.args.get('id', default = None, type = int)
    raidId = request.args.get('raidId', default = None, type = int)
    status = request.args.get('status', default = None, type = str)
    partyId = request.args.get('partyId', default = None, type = int)
    return game_controller.getGame(id, raidId, status, partyId)


@app.route('/game', methods=['POST'])
def addGame(request):
    """
    endpoint to add a new game from a submitted json request
    required input:
    {
        "raidId": raidId
        "partyId": partyId
        "status": status
    }
        ApiNote:
                POST /game
    """
    partyId = request.args.get('raidId', default = None, type = int)
    raidId = request.args.get('partyId', default = None, type = int)
    status = request.args.get('status', default = None, type = str)
    return game_controller.addGame(raidId,partyId,status)
