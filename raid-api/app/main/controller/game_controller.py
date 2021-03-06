from flask import jsonify
from app import app, db, ma
import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from app.main.model.game import *
from app.main.model.party_user import *
from app.main.model.party import *
from app.main.model.user import *
from app.main.model.phase import *


def getGame(id, raidId, status, partyId):
    """
        Controller method to get a single game with given id.

        Args:
                id: Id of the party to be found.
        """

    query = db.session.query(Game.id, Game.status, Game.timeCreated, Party.sherpa, Phase.name,
                              User.id, User.displayName , PartyUser.leader, PartyUser.status)\
                                  .join(Party.games)\
                                      .join(Party.partyUsers)\
                                          .join(User)\
                                              .join(Phase)
    if (id != None):
        query = query.filter(Game.id == id)
    if (raidId != None):
        query = query.filter(Game.raidId == raidId)
    if (status != None):
        query = query.filter(Game.status == status)
    if (partyId != None):
        query = query.filter(Game.partyId == partyId)
    
    result = query.all()

    if len(result) == 0:
        return "Games not found", 404
    result = Game.gameJsonParsing(result)
    return jsonify(result)


def addGame(user, raidId, partyId, status, phaseId):
    """
    method to add a new game from a submitted json request
    required input:
    {
        "raidId": raidId
        "partyId": partyId
        "status": status
    }
    """

    query = PartyUser.query
    query = query.filter(PartyUser.userId == user.id)
    query = query.filter(PartyUser.leader == True)
    query = query.filter(PartyUser.partyId == partyId)
    partyUser_result = query.all()
    if len(partyUser_result) != 1:
        return "party not found or not leader", 404
    new_game = Game(raidId, partyId, status, phaseId)
    db.session.add(new_game)
    try:
        db.session.commit()
    except exc.OperationalError:
        return "Database error", 500
    return {"gameId": new_game.id}


def deleteGame(gameId):
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
    return "Game Deleted", 200
