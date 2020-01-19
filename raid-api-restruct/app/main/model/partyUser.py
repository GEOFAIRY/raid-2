from app import db, ma


"""PartyUser information handler"""


class PartyUser(db.Model):
    """
    class for storing partyUser data
    args:
        id - Unique PartyUser identifier Int()
        partyId - party identifier Int()
        userId - user identifier Int()
        leader - if the user is a party leader Bool()
        status - the current party status Str()
    """
    id = db.Column(db.Integer, primary_key=True)
    partyId = db.Column(db.Integer, db.ForeignKey('Party.id'))
    userId = db.Column(db.Integer, db.ForeignKey('User.id'))
    leader = db.Column(db.Boolean)
    status = db.Column(db.String)

    def __init__(self, partyId, userId, leader, status):
        self.partyId = partyId
        self.userId = userId
        self.leader = leader
        self.status = status


class PartyUserSchema(ma.Schema):
    """class for parsing partyUser data"""
    class Meta:
        fields = ('id', 'partyId', 'userId', 'leader', 'status')


# init schemas
partyUserSchema = PartyUserSchema()
partyUsersSchema = PartyUserSchema(many=True)