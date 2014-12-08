#!flask/bin/python
from flask import Flask, jsonify, request, abort
from sampleNeighbors import sampleNeighborsJSON
import accessMethods as am

app = Flask(__name__)

@app.route('/getNeighbors', methods=['GET','POST'])
def getNeighbors():
    # show the user profile for that user
    lon = request.args.get('lon')
    lat = request.args.get('lat')
    r = sampleNeighborsJSON
    return jsonify({'result': r}), 201

@app.route('/getCalories', methods=['GET'])
def getCalories():
    # if not request.get_json(force=True) or not 'text' in request.get_json(force=True):
    #     print 'aborting'
    #     abort(400)
    q = request.args.get('q')
    r = am.getCalories(q)
    print r

    return jsonify({'result': r}), 201

@app.route('/getFloorsTimeSeries', methods=['GET'])
def getFloorsTimeSeries():


    r = am.getFloorsTimeSeries()

    return jsonify({'result': r}), 201

if __name__ == '__main__':
    app.run(debug=True)
