from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'database_name'
app.config['MONGO_URI'] = 'database_uri'

mongo = PyMongo(app)

@app.route('/results', methods=['GET'])
def get_all_results():
  for s in results.find():
    try:
      object_id= s['_id']
      id =  str(object_id)
      s['_id'] = id
    except KeyError :
      continue;
    output.append(s)
  return jsonify({'result' : output})

@app.route('/result/<device_id>', methods=['GET'])
def get_one_result(device_id):
  s = results.find({'device_id' : device_id})
  for result in s:
    if result:
      object_id= result['_id']
      id =  str(object_id)
      result['_id'] = id
      output.append(result)
    else:
      output.append("No Result Found")
  return jsonify({'result' : output})

@app.route('/result/<firmware_version>/<device_id>', methods=['GET'])
def get_device_result(firmware_version , device_id ):
  s = results.find( { '$and': [{ 'firmware_version' : firmware_version } , { 'device_id': device_id }] })
  for result in s:
    if result:
      object_id= result['_id']
      id =  str(object_id)
      result['_id'] = id
      output.append(result)
    else:
      output.append("No Result Found")
  return jsonify( output)

if __name__ == '__main__':
    output = []
    results = mongo.db.collection_name
    app.run(host='0.0.0.0',debug=True)