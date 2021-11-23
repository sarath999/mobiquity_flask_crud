"""
    This module used to perform crud operations on atm datset based user inputs
"""
import json
from flask import Flask, render_template, request, Response, jsonify

import requests

from utils import ATMS, user_validator, get_atm_by_uid, get_atm_by_addr

app = Flask(__name__, static_url_path='/static')


@app.route('/data_invoke')
def load_data():
    """
        To invoke the ATMs dataset from https://www.ing.nl/api/locator/atms/
    """
    atms = requests.get("https://www.ing.nl/api/locator/atms/").text
    #print(atms)
    raw_data = json.dumps(atms)
    atms_json = json.loads(raw_data)[6:]
    #data = json.loads(atms_json)
    print(type(atms_json))
    return atms_json

@app.route('/')
def index():
    """
        To render the base template
    """
    #f = open('data.json',)

    # returns JSON object as
    # a dictionary
    #data = json.load(f)

    # Iterating through the json
    # list
    # for i in data:
    #     print(i,)
    #global ATMS;
    #ATMS = data
    # Closing file
    #f.close()
    #return jsonify(data)
    return render_template("index.html", len = len(ATMS), atms = ATMS)


@app.route('/api/add_atm', methods=['POST'])
def add_atm():
    """
        This method used for add new ATM
        Expected Input should be json with all thee required parmetrs.

        Expected Output
    """
    user = user_validator(request.authorization["username"], request.authorization["password"])

    input_data = request.json
    if user:
        if input_data:
            check = get_atm_by_addr(input_data["address"])
            if not check:
                # print(uuid.uuid4())
                input_data["uid"] = len(ATMS)+1

                ATMS.append(input_data)
                response = Response("ATM added successfully", 201, mimetype='application/json')
            else:
                response = Response("This ATM already added", 200, mimetype='application/json')
        else:
            response = Response("Input data should not be empty", 200, mimetype='application/json')
    else:
        response = Response("User not authenticated", 200, mimetype='application/json')


    return response



@app.route('/api/get_atm/<uid>', methods=['GET'])
def get_atm(uid):
    """
        To get the single ATM info
    """
    user = user_validator(request.authorization["username"], request.authorization["password"])
    if user:
        atm = get_atm_by_uid(uid)
        if atm:
            response = jsonify(atm)
        else:
            response = Response("data not found", 200, mimetype='application/json')
    else:
        response = Response("User not authenticated", 200, mimetype='application/json')

    return response

@app.route('/api/update_atm', methods=['PUT'])
def update_atm():
    """
        To update the single ATM information
    """
    user = user_validator(request.authorization["username"], request.authorization["password"])

    input_data = request.json
    if user:
        if input_data:
            atm = get_atm_by_uid(input_data["uid"])
            if atm:
                ATMS.remove(atm)
                ATMS.append(input_data)
                response = Response("ATM Info Updated", 200, mimetype='application/json')
            else:
                response = Response("ATM Not Found", 200, mimetype='application/json')
        else:
            response = Response("Input data should not be empty", 200, mimetype='application/json')
    else:
        response = Response("User not authenticated", 200, mimetype='application/json')


    return response

@app.route('/api/delete_atm/<uid>', methods=['DELETE'])
def delete_atm(uid):
    """
        To Delete the single ATM info
    """
    user = user_validator(request.authorization["username"], request.authorization["password"])
    if user:
        atm = get_atm_by_uid(uid)
        if atm:
            ATMS.remove(atm)
            response = Response("ATM deleted successfully", 200, mimetype='application/json')
        else:
            response = Response("atm not found", 200, mimetype='application/json')
    else:
        response = Response("User not authenticated", 200, mimetype='application/json')

    return response

if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)
