from app import app, db, ma, auth
import os

from flask import Flask, jsonify, request, g
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

import datetime

"""Party information hangler"""


class Parties(db.Model):
    """
    class for storing party data
    args:
        partyId - Unique party identifier Int()
        raidId - Unique raid identifier FOREIGN KEY raids.id
        user1Id - party leader FOREIGN KEY users.id
        user2Id - party member FOREIGN KEY users.id
        user3Id - party member FOREIGN KEY users.id
        user4Id - party member FOREIGN KEY users.id
        user5Id - party member FOREIGN KEY users.id
        user6Id - party member FOREIGN KEY users.id
        phase - the phase the party is recruiting for Int()
        sherpa - if the raid is a sherpa raid Bool()
    """
    partyId = db.Column(db.Integer, primary_key=True)
    raidId = db.Column(db.Integer, db.ForeignKey('raids.id'), nullable=False)
    status = db.Column(db.String, nullable=False)
    user1Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user2Id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user3Id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user4Id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user5Id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user6Id = db.Column(db.Integer, db.ForeignKey('users.id'))
    phase = db.Column(db.Integer, nullable=False)
    sherpa = db.Column(db.Boolean, nullable=False)
    timeCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    raid = db.relationship("Raids", foreign_keys=[raidId])
    user1 = db.relationship("Users", foreign_keys=[user1Id])
    user2 = db.relationship("Users", foreign_keys=[user2Id])
    user3 = db.relationship("Users", foreign_keys=[user3Id])
    user4 = db.relationship("Users", foreign_keys=[user4Id])
    user5 = db.relationship("Users", foreign_keys=[user5Id])
    user6 = db.relationship("Users", foreign_keys=[user6Id])

    def __init__(self, raidId, status, user1Id, phase, sherpa):
        self.raidId = raidId
        self.status = status
        self.user1Id = user1Id
        self.phase = phase
        self.sherpa = sherpa


class PartiesSchema(ma.Schema):
    """class for parsng party data"""
    class Meta:
        fields = ('partyId', 'raidId', 'status', 'user1Id', 'user2Id',
                  'user3Id', 'user4Id', 'user5Id', 'user6Id', 'phase', 'sherpa', 'timeCreated')


# init schemas
partySchema = PartiesSchema()
partiesSchema = PartiesSchema(many=True)


@app.route('/party', methods=['POST'])
@auth.login_required
def addParty():
    """

    """
    raidId = request.json['raidId']
    status = request.json['status']
    user1Id = g.user.id
    phase = request.json['phase']
    sherpa = request.json['sherpa']

    new_party = Parties(raidId, status, user1Id, phase, sherpa)

    db.session.add(new_party)
    try:
        db.session.commit()
    except exc.OperationalError:
        return "Database error", 500

    return partySchema.jsonify(new_party), 201


@app.route('/parties', methods=['GET'])
@auth.login_required
def getParties():
    """

    """
    allParties = Parties.query.all()
    result = partiesSchema.dump(allParties)
    return jsonify(result)


@app.route('/party/<partyId>', methods=['GET'])
@auth.login_required
def getParty(partyId):
    """

    """
    party = Parties.query(Parties.partyId, Parties.raid.id, Parties.status, Parties.user1.id, Parties.user1.displayName,
                          Parties.user2.id, Parties.user2.displayName, Parties.user3.id, Parties.user3.displayName,
                          Parties.user4.id, Parties.user4.displayName, Parties.user5.id, Parties.user5.displayName,
                          Parties.user6.id, Parties.user6.displayName, Parties.phase, Parties.sherpa, Parties.timeCreated)\
                              .get(partyId)
    if party == None:
        return "party not found", 404
    return partySchema.jsonify(party)


@app.route('/join/<partyId>', methods=['PATCH'])
@auth.login_required
def joinParty(partyId):
    """

    """
    party = Parties.query.get(partyId)
    userId = g.user.id

    if party.user2Id == None:
        party.user2Id = userId
    elif party.user3Id == None:
        party.user3Id = userId
    elif party.user4Id == None:
        party.user4Id = userId
    elif party.user5Id == None:
        party.user5Id = userId
    elif party.user6Id == None:
        party.user6Id = userId
    else:
        return "party full", 400

    db.session.commit()

    return partySchema.jsonify(party)
