from app import app, db, ma, auth
from app.main.model import *
import os

from flask import Flask, jsonify, request, g
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from passlib.hash import sha256_crypt
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

import datetime

"""User information handler"""



class User(db.Model):
    """
    class for storing raid data
    args:
        id - Unique user identifier Int()
        steamId - Unique steam user identifier Str()
        password - Hash of user submitted password Str()
        displayName - Destiny 2 display name Str()
        email - Unique email that conforms with email address standards Str()
        timeCreated - the time created DateTime()
    """
    id = db.Column(db.Integer, primary_key=True)
    steamId = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    displayName = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    timeCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    partyUser = db.relationship('PartyUser', backref='user', lazy=True)


    def __init__(self, steamId, password, displayName, email):
        self.steamId = steamId
        self.password = self.encrypt(password)
        self.displayName = displayName
        self.email = email

    def encrypt(self, password):
        return sha256_crypt.encrypt(password)

    def verify(self, password):
        return sha256_crypt.verify(password, self.password)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user

class UserSchema(ma.Schema):
    """class for parsing user data"""
    class Meta:
        fields = ('id', 'steamId', 'password', 'displayName', 'email', 'timeCreated')


#init schemas
userSchema = UserSchema()
usersSchema = UserSchema(many=True)