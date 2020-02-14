from app import app, db, ma, auth
import os

from flask import Flask, jsonify, request, g
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from passlib.hash import sha256_crypt
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

import datetime

from app.main.model.user import *


def getUser(id, steamId, displayName, email):
    """
    get users with or without search params
    params:
        - id
        - steamId
        - displayName
        - email

    returns:
        - an array in json format of the users
    """

    #build query based of params submitted
    query = User.query
    if (id != None):
        query = query.filter(User.id == id)
    if (steamId != None):
        query = query.filter(User.steamId == steamId)
    if (displayName != None):
        query = query.filter(User.displayName == displayName)
    if (email != None):
        query = query.filter(User.email == email)

    allUsers = query.all()
    user_schema = UserSchema(many=True, only=("id", "steamId", "displayName", "timeCreated"))
    result = user_schema.dump(allUsers)

    #format json to return
    if len(result) == 0:
        return "Users not found", 404
    return jsonify(result)


def addUser(steamId, password, displayName, email):
    """
    method to add a new user from a submitted json request
    required input:
    {
        "steamId": steamId
        "password": password
        "displayName": displayName
        "email": email
    }

    returns:
        -the id of the new user
    """

    #validate email
    if (not User.emailValid(email)):
        print("email 1")
        return "Email Invalid", 400
    if email is None or password is None:
        print("email or password")
        return "Missing args", 400 # missing arguments

    new_user = User(steamId, password, displayName, email)

    #commit user to database
    db.session.add(new_user)
    try:
        db.session.commit()
    except exc.OperationalError:
        return "Database error", 500
    except exc.IntegrityError:
        return "Steam ID or Email already registered", 400

    return { "id": new_user.id }, 201


@auth.verify_password
def verify_password(email_or_token, password):
    """method to check a users login credentials
    
    Arguments:
        email_or_token {String} -- a string which could be a token or email
        password {String} -- the raw password to check if needed
    
    Returns:
        Boolean -- whether the login credentials are valid
    """    
    # first try to authenticate by token
    user = User.verify_auth_token(email_or_token)
    if not user:
        # try to authenticate with email/password
        user = User.query.filter_by(email = email_or_token).first()
        if not user or not user.verify(password):
            return False
    g.user = user
    return True


@auth.login_required
def get_auth_token():
    """method to create a new token for the /token endpoint
    
    Returns:
        Dict -- a json format containing the new token as a string
    """    
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') }), 201