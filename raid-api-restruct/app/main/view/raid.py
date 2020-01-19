from flask import jsonify

from app import app
from app.main.model import raid as RaidModel


@app.route('/raids', methods=['GET'])
def getRaids():
    """endpoint to return all raid data"""
    allRaids = RaidModel.Raid.query.all()
    result = RaidModel.raidsSchema.dump(allRaids)
    return jsonify(result)


@app.route('/raids/<searchId>', methods=['GET'])
def getRaid(searchId):
    """endpoint to return a single raids data"""
    raid = RaidModel.Raid.query.get(searchId)
    if raid is None:
        return "raid not found", 404
    return RaidModel.raidSchema.jsonify(raid)
