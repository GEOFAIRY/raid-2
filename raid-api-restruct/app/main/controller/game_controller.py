from flask import jsonify
from app import app, db, ma
import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.main.model.game import *


def getGames():
	"""
	Controller method to get all currently available games.
	"""
    allGames = Game.query.all()
    result = gameSchema.dump(allGames)
    return jsonify(result)


def getGameById(id):
    """
	Controller method to get a single game with given id.

	Args:
		id: Id of the game to be found.
	"""
    gameSearched = Game.query.get(id)
    if gameSearched == None:
        return "Game not found", 404
    return gameSchema.jsonify(gameSearched)

def addGame(request):
    """
    method to add a new game from a submitted json request
    required input:
    {
        "raidId": raidId
        "partyId": partyId
        "status": status
    }
    """
    raidId = request.json['raidId']
    partyId = request.json['partyId']
    status = request.json['status']

    new_game = Game(raidId, partyId, status)