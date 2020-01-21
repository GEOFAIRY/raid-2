from app import app, db, ma, auth
import os
from app.helpers import emails

from flask import Flask, jsonify, request, g
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from passlib.hash import sha256_crypt
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

import datetime


def getUser(request):
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
    if len(result) == 0:
        return "Users not found", 404
    for i in result:
        del i["password"]
        del i["email"]
    return jsonify(result)


def addUser(request):
    """
    method to add a new user from a submitted json request
    required input:
    {
        "steamId": steamId
        "password": password
        "displayName": displayName
        "email": email
    }
    """
    steamId = request.json['steamId']
    password = request.json['password']
    displayName = request.json['displayName']
    email = request.json['email']

    #validate email
    if (not emails.emailValid(email)):
        print("email 1")
        return "Email Invalid", 400
    if email is None or password is None:
        print("email or password")
        return "Missing args", 400 # missing arguments

    new_user = Users(steamId, password, displayName, email)

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
    # first try to authenticate by token
    user = Users.verify_auth_token(email_or_token)
    if not user:
        # try to authenticate with email/password
        user = Users.query.filter_by(email = email_or_token).first()
        if not user or not user.verify(password):
            return False
    g.user = user
    return True


@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') }), 201