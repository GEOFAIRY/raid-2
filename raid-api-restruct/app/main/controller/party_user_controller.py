from flask import jsonify
from app import app, db, ma
import os

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.main.model.party_user import *



def addPartyUser(request):
    """
    method to add a new party user from a submitted json request
    required input:
    {
        "partyId": partyId
        "userId": userId
        "status": status
		"leader": leader
    }
    """
    partyId = request.json['partyId']
    userId = request.json['userId']
    status = request.json['status']
	leader = request.json['leader']

    new_party_user = Game(partyId, userId, leader, status)