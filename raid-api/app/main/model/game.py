from app import db, ma

import datetime

"""Game information handler"""


class Game(db.Model):
    """
    class for storing game data
    args:
        id - unique identifier Int()

    """
    id = db.Column(db.Integer, primary_key=True)
    raidId = db.Column(db.Integer, db.ForeignKey('raid.id'))
    status = db.Column(db.String)
    partyId = db.Column(db.Integer, db.ForeignKey('party.id'))
    timeCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)


    def __init__(self, raidId, partyId, status):
        self.raidId = raidId
        self.partyId = partyId
        self.status = status


class GameSchema(ma.Schema):
    """class for parsing game data correctly"""

    class Meta:
        fields = ('id', 'raidId', 'partyId', 'status', 'timeCreated')


# init schemas
gameSchema = GameSchema()
gamesSchema = GameSchema(many=True)
