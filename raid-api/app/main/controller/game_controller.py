from flask import jsonify
from app import app, db, ma
import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.main.model.game import *


def getGame(id, raidId, status, partyId):
    """
	Controller method to get a single game with given id.

	Args:
		id: Id of the party to be found.
	"""
    query =  Game.query
    if (id != None):
        query = query.filter(Game.id == id)
    if (raidId != None):
        query = query.filter(Game.raidId == raidId)
    if (status != None):
        query = query.filter(Game.status == status)
    if (partyId != None):
        query = query.filter(Game.partyId == partyId)


    allGames = query.all()
    result = gameSchema.dump(allGames)
    if len(result) == 0:
        return "Games not found", 404
    print(result)
    return jsonify(result)


def addGame(raidId,partyId,status):
    """
    method to add a new game from a submitted json request
    required input:
    {
        "raidId": raidId
        "partyId": partyId
        "status": status
    }
    """
    new_game = Game(raidId, partyId, status)
    db.session.add(new_game)
    try:
        db.session.commit()
    except exc.OperationalError:
        return "Database error", 500
    return { "gameId": new_game.id }

def leaveGame(userId,gameId):
    """
    method to close a game
    Args:
        gameId: id of game to close
    """
    query = Game.query
    query = query.filter(Game.gameId == gameId)
    allGames = query.all()
    result = gameSchema.dump(allGames)
     try:
        db.session.delete(result)
    except exc.OperationalError:
        return "Database error", 500
    return { "Game is deleted with id of ": gameId}
    