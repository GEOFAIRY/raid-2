from app import app, db, ma
import os
from app.helpers import passwords, emails

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

"""User information handler"""

class Users(db.Model):
    """
    class for storing raid data
    args:
        id - Unique user identifier Int()
        steamId - Unique steam user identifier Str()
        password - Hash of user submitted password Str()
        displayName - Destiny 2 display name Str()
        email - Unique email that conforms with email address standards Str()
    """
    id = db.Column(db.Integer, primary_key=True)
    steamId = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    displayName = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)



    def __init__(self, steamId, password, displayName, email):
        self.steamId = steamId
        self.password = password
        self.displayName = displayName
        self.email = email


class UsersSchema(ma.Schema):
    """class for parsing user data"""
    class Meta:
        fields = ('id', 'steamId', 'password', 'displayName', 'email')


#init schemas
userSchema = UsersSchema()
usersSchema = UsersSchema(many=True)


@app.route('/users', methods=['GET'])
def getUser():
    """
    get users with or without search params
    params:
        - id
        - steamId
        - displayName
        - email
    """
    id = request.args.get('id', default = None, type = int)
    steamId = request.args.get('steamId', default = None, type = str)
    displayName = request.args.get('displayName', default = None, type = str)
    email = request.args.get('email', default = None, type = str)

    #build query based of params submitted
    query = Users.query
    if (id != None):
        query = query.filter(Users.id == id)
    if (steamId != None):
        query = query.filter(Users.steamId == steamId)
    if (displayName != None):
        query = query.filter(Users.displayName == displayName)
    if (email != None):
        query = query.filter(Users.email == email)

    allUsers = query.all()
    result = usersSchema.dump(allUsers)

    #format json to return
    if (len(result) == 1):
        del result[0]["password"]
        del result[0]["email"]
        return jsonify(result[0])
    for i in result:
        del i["password"]
        del i["email"]
    return jsonify(result)


@app.route('/users', methods=['POST'])
def addUser():
    """
    endpoint to add a new user from a submitted json request
    required input:
    {
        "steamId": steamId
        "password": password
        "displayName": displayName
        "email": email
    }
    """
    steamId = request.json['steamId']
    password = passwords.encrypt(request.json['password'])
    displayName = request.json['displayName']
    email = request.json['email']

    #validate email
    if (not emails.emailValid(email)):
        return "Email Invalid", 400
    
    new_user = Users(steamId, password, displayName, email)

    #commit user to database
    db.session.add(new_user)
    try:
        db.session.commit()
    except exc.OperationalError:
        return "Database error", 500
    except exc.IntegrityError:
        return "Steam ID or Email already registered", 400

    return { "id": new_user.id }