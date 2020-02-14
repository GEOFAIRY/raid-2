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

    def gameJsonParsing(json):
        result = []
        gameExists = False
        for i in json:
            for j in result:
                if j["id"] == i[0]:
                    gameExists = True
                    j["users"].append({"id": i[4], "leader": i[5], "status": i[6]})
            if not gameExists:
                newEntry = {"id": i[0], "status": i[1], "created": i[2], "sherpa": i[3], "users": [{"id": i[4], "leader": i[5], "status": i[6]}]}
                result.append(newEntry)
        return result


class GameSchema(ma.Schema):
    """class for parsing game data correctly"""

    class Meta:
        fields = ('id', 'raidId', 'partyId', 'status', 'timeCreated')


# init schemas
gameSchema = GameSchema()
gamesSchema = GameSchema(many=True)
