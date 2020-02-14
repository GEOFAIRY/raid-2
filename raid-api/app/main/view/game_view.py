from flask import jsonify, request, g

from app import app, auth
from app.main.controller import game_controller





@app.route('/game', methods=['GET'])
@auth.login_required
def getGame():
    """endpoint to return a single games data
        ApiNote:
                        GET /game/:id
        Args:
                id: The id of the desired game to be found.
                raidId: The raid id to filter by
                status: the game status to filter by
                partyId: the party id to filter by
        Returns:
                game of entered id in Json format.
        """

    id = request.args.get('id', default = None, type = int)
    raidId = request.args.get('raidId', default = None, type = int)
    status = request.args.get('status', default = None, type = str)
    partyId = request.args.get('partyId', default = None, type = int)
    return game_controller.getGame(id, raidId, status, partyId)


@app.route('/game', methods=['POST'])
@auth.login_required
def addGame():
    """
    endpoint to add a new game from a submitted json request
    required input:
    {
        "raidId": raidId
        "partyId": partyId
        "status": status
        "phaseId": phaseId
    }
        ApiNote:
                POST /game
    """
    user = g.user
    partyId = request.json['raidId']
    raidId = request.json['partyId']
    status = request.json['status']
    phaseId = request.json['phaseId']
    return game_controller.addGame(user, raidId, partyId, status, phaseId    )


@app.route('/game/leave', methods=['GET'])
@auth.login_required
def leaveGame():
    """
    endpoint to leave a game from a submitted json request
    required input:
    {
        "gameId": gameId
    }
        ApiNote:
                POST /game
    """
    user = g.user
    gameId = request.args.get('gameId', default = None, type = int)
    return game_controller.leaveGame(user, gameId)
