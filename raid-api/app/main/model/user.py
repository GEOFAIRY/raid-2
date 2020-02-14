from app import app, db, ma

from marshmallow import fields
from passlib.hash import sha256_crypt
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from validate_email import validate_email

import datetime

from app.main.model.party_user import PartyUser, PartyUserSchema

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

    partyUsers = db.relationship('PartyUser', backref='user', lazy=True)

    def __init__(self, steamId, password, displayName, email):
        self.steamId = steamId
        self.password = self.encrypt(password)
        self.displayName = displayName
        self.email = email

    def verify(self, password):
        """method to verify a given password with a stored hash
        
        Arguments:
            password {string} -- the password to check
        
        Returns:
            Boolean -- whether the password matches the hash
        """        
        return sha256_crypt.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        """method to generate a new auth token
        
        Keyword Arguments:
            expiration {int} -- the time until the token expires (default: {600})
        
        Returns:
            string -- the token generated
        """        
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    def encrypt(self, password):
        """method to encrypt a given password
        
        Arguments:
            password {String} -- the password to encrypt
        
        Returns:
            String -- the encrypted password
        """        
        return sha256_crypt.encrypt(password)

    def emailValid(email):
        """method to validate a given email
        
        Arguments:
            email {String} -- the email to verify
        
        Returns:
            Boolean -- whether the email is valid or not
        """        
        return validate_email(email)

    @staticmethod
    def verify_auth_token(token):
        """method to check if a token is legitimate
        
        Arguments:
            token {String} -- the token to check
        
        Returns:
            User -- the user with the matching token
        """        
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


class UserSchema(ma.Schema):
    """class for parsing user data"""

    class Meta:
        fields = ('id', 'steamId', 'password', 'displayName', 'email', 'timeCreated')


# init schemas
userSchema = UserSchema()
usersSchema = UserSchema(many=True)
