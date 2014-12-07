#!flask/bin/python
from flask import Flask, jsonify, request, abort
import accessMethods as am

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

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
