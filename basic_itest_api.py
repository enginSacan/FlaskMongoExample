from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

"""
 This file is created to demonstrate the flask api with mongo database.
 
 To configuring the Mongo database you need to name first with Flask and then give the database name and uri
 
 This file return the results of the tests that is related with the devices. Table columns and names could be change.
"""


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'database_name'
app.config['MONGO_URI'] = 'database_uri'

mongo = PyMongo(app)


@app.route('/results', methods=['GET'])
def get_all_results():
    """
    This function is specified the path of the device results
    :return: JSON object of the results
    """
    for s in results.find():
        try:
            object_id = s['_id']
            id = str(object_id)
            s['_id'] = id
        except KeyError:
            continue;
        output.append(s)
    return jsonify({'result': output})


@app.route('/result/<device_id>', methods=['GET'])
def get_one_result(device_id):
    """
    This function is specified the path of the device results for specific device
    :param device_id: device id for the that specified
    :return: JSON object of the results
    """
    s = results.find({'device_id': device_id})
    for result in s:
        if result:
            object_id = result['_id']
            id = str(object_id)
            result['_id'] = id
            output.append(result)
        else:
            output.append("No Result Found")
    return jsonify({'result': output})


@app.route('/result/<firmware_version>/<device_id>', methods=['GET'])
def get_device_result(firmware_version, device_id):
    """
    This function is specified the path of the device results with specified firmware versions
    :param firmware_version: firmware version that needed
    :param device_id: device id for the that specified firmware versions
    :return: JSON object of the results
    """
    s = results.find({'$and': [{'firmware_version': firmware_version}, {'device_id': device_id}]})
    for result in s:
        if result:
            object_id = result['_id']
            id = str(object_id)
            result['_id'] = id
            output.append(result)
        else:
            output.append("No Result Found")
    return jsonify(output)


if __name__ == '__main__':
    output = []
    results = mongo.db.collection_name
    app.run(host='0.0.0.0', debug=True)
