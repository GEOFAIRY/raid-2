from flask import jsonify, request

from app import app, auth
from app.main.controller import user_controller



@app.route('/users', methods=['GET'])
def getUser():
    """
    endpoint to get users with or without search params
    ApiNote:
        GET /users
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

    return user_controller.getUser(id, steamId, displayName, email)



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
    ApiNote:
        POST /users
    """
    steamId = request.json['steamId']
    password = request.json['password']
    displayName = request.json['displayName']
    email = request.json['email']

    return user_controller.addUser(steamId, password, displayName, email)




@app.route('/token')
@auth.login_required
def get_auth_token():
    """
    endpoint to create an auth token for a logged in user.
    ApiNote:
        GET /token
    """
    return user_controller.get_auth_token()