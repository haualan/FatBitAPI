#!flask/bin/python
from tinydb import TinyDB, where 
from flask import Flask, jsonify, request, abort
from sampleNeighbors import sampleNeighborsJSON
import accessMethods as am

dBString = '/var/www/jpmcResearchBot/FatBitAPI/db.json'
scoreDBstring = '/var/www/jpmcResearchBot/FatBitAPI/score.json'

# dBString = 'db.json'
# scoreDBstring = 'score.json'

app = Flask(__name__)

@app.route('/getNeighbors', methods=['POST'])
def getNeighbors():
    # save the user location in some DB, TBD (...maybe tinyDB)
    iJSON = request.get_json(force=True)

    

    db = TinyDB(dBString)
    # db.insert(iJSON)


    if db.search(where('UID') == iJSON['UID']):
        # do update
        db.update(iJSON, where('UID') == iJSON['UID'])
    else:
        # fresh user, insert location
        db.insert(iJSON)
    
    db.close()

    

    lon = request.args.get('lon')
    lat = request.args.get('lat')
    r = sampleNeighborsJSON
    return jsonify({'result': r}), 201


@app.route('/postOutcome', methods=['POST'])
def postOutcome():
    iJSON = request.get_json(force=True)
    score = iJSON['score']
    UID = iJSON['UID']

    db = TinyDB(scoreDBstring)
    # db.insert(iJSON)


    if db.search(where('UID') == UID):
        # do update
        f = db.search(where('UID') == UID)
        newscore = int(f[0]['score']) + int(score)
        db.update({"score": newscore}, where('UID') == iJSON['UID'])
    else:
        # fresh user, insert location
        db.insert(iJSON)
    
    db.close()

    return jsonify({'result': 201}), 201

@app.route('/getLeaders', methods=['GET'])
def getLeaders():
    db = TinyDB(scoreDBstring)

    # just return the top 5 winners
    r = []
    for i in db.all():
      print i
      r.append([i['UID'],i['score']])

    r = sorted(r, key = lambda x: x[1], reverse = True)[0:5]

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
