from app import db, ma

"""Phase information handler"""


class Phase(db.Model):
    """
    class for storing phase data
    args:
        id - unique identifier Int()
        raidId - the raid id associated with the raid phase Int()
        order - the order in the phases of this phase e.g. 2nd Int()
        name - the raid name Str()
    """
    id = db.Column(db.Integer, primary_key=True)
    raidId = db.Column(db.Integer, db.ForeignKey('raid.id'))
    order = db.Column(db.Integer)
    name = db.Column(db.String)

    def __init__(self, raidId, order, name):
        self.raidId = raidId
        self.order = order
        self.name = name


class PhaseSchema(ma.Schema):
    """class for parsing phase data correctly"""

    class Meta:
        fields = ('id', 'raidId', 'order', 'name')


# init schemas
phaseSchema = PhaseSchema()
phasesSchema = PhaseSchema(many=True)
