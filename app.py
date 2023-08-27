# import de mes librairies
import collections
from flask import Flask, jsonify, request
import os

from pymongo import MongoClient
from bson.objectid import ObjectId

# création de mon application flask
app = Flask(__name__)

host = os.environ.get("MONGO_HOST","localhost")
port = 27017
# création du client de connexion
client = MongoClient(host=host, port=port)

# récupération de ma db
mabdd = client.demo

# première route sur "/"
@app.route("/")
def hello_world():
    informations = "Hello, World! \n mabdd_type : \n"+str(type(mabdd)) + " \n mabdd : \n" +mabdd
    return informations
# test flask 123
@app.route("/poulet", methods=["GET"])
def poulet(msg):
    return f'bonjour {msg}'

# méthode read all
@app.route("/users", methods=["GET"])
def get_users():
    datas= list(col.find())
    for data in datas:
        data["_id"] = str(data["_id"])
    return jsonify({"users": datas})

# méthode find by id
@app.route("/users<id>", methods=["GET"])
def get_user(id):
    data = col.find_one({'_id': ObjectId(id)})
    data['_id'] = str(data["_id"])
    return jsonify({"users": data})

# méthode pour créer un user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    result = col.insert_one(data)
    data['_id'] = str(result.inserted_id)
    return jsonify({"new_user": data})

# méthode pour mettre à jour
@app.route("/users<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    data ['_id'] = ObjectId(id)
    result = col.replace_one({'_id': ObjectId(id)}, data)
    data['_id'] = str(result.upserted_id)
    return jsonify({"update_user", data})

# méthode pour delete
@app.route("/users<id>", methods=["DELETE"])
def delete_user(id):
    data = request.get_json()
    data ['_id'] = ObjectId(id)
    data_delete = col.find_one({'_id': ObjectId(id)}, data)
    col.delete_one({'_id': ObjectId(id)}, data)
    return jsonify({"delete_user :", data_delete})

# lancement de mon app
if __name__=="__main__":
    app.run(host="0.0.0.0", port=9001, debug=True)