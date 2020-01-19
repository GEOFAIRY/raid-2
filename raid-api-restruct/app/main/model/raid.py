from app import db, ma

"""Raid information handler"""


class Raid(db.Model):
    """
    class for storing raid data
    args:
        id - unique identifier Int()
        name - the raid name Str()
        image - url to raid banner image Str()
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)

    phases = db.relationship('Phase', backref='raid', lazy=True)
    games = db.relationship('Game', backref='raid', lazy=True)

    def __init__(self, name, image):
        self.name = name
        self.image = image


class RaidSchema(ma.Schema):
    """class for parsing raid data correctly"""
    class Meta:
        fields = ('id', 'name', 'image')


#init schemas
raidSchema = RaidSchema()
raidsSchema = RaidSchema(many=True)

import app.main.view.raid