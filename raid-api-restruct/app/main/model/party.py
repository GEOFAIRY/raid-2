from app import db, ma

import datetime

"""Party information handler"""


class Party(db.Model):
    """
    class for storing party data
    args:
        partyId - Unique party identifier Int()
        sherpa - if the raid is a sherpa raid Bool()
        timeCreated - the time created DateTime()
    """
    partyId = db.Column(db.Integer, primary_key=True)
    sherpa = db.Column(db.Boolean, nullable=False)
    timeCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    game = db.relationship('Game', backref='party', lazy=True)
    partyUser = db.relationship('PartyUser', backref='party', lazy=True)

    def __init__(self, raidId, sherpa):
        self.raidId = raidId
        self.sherpa = sherpa


class PartySchema(ma.Schema):
    """class for parsing party data"""

    class Meta:
        fields = ('partyId', 'sherpa', 'timeCreated')


# init schemas
partySchema = PartySchema()
partiesSchema = PartySchema(many=True)
