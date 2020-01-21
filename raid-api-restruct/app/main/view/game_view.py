from flask import jsonify

from app import app
from app.main.model import game
from app.main.controller import game_controller


@app.route('/game', methods=['GET'])
def getGames():
    """
    endpoint to get all games
        ApiNote:
                GET /users
    """
    return game_controller.getGames()


@app.route('/game/<id>', methods=['GET'])
def getGame(id):
    """endpoint to return a single games data
        ApiNote:
                        GET /game/:id
        Args:
                id: The id of the desired game to be found.
        Returns:
                game of entered id in Json format.
        """
    return game_controller.getGameById(id)


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
    return game_controller.addGame(request)
