from flask import jsonify

from app import app, auth
from app.main.controller import user_controller



@app.route('/users', methods=['GET'])
def getUser(request):
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
    return user_controller.getUser(request)



@app.route('/users', methods=['POST'])
def addUser(request):
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
    return user_controller.addUser(request)




@app.route('/token')
@auth.login_required
def get_auth_token():
    """
    endpoint to create an auth token for a logged in user.
    ApiNote:
        GET /token
    """
    return user_controller.get_auth_token()