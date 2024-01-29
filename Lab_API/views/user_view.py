from flask import Blueprint, request, jsonify
from database.__init__ import database
from models.user_model import User
import json
from bson.objectid import ObjectId

user = Blueprint("user", __name__)


#@user.route("/v0/users/", methods=["POST"])
@user.route("/v1/users/", methods=["POST"])
def create():

    data = json.loads(request.data)
    print(data)

    my_user = User()

    #my_user.name = "Renan"
    #my_user.email = "renan@gmail.com"
    #my_user.password = "123456"
    #print(my_user.__dict__)

    my_user.name = data["name"]
    my_user.email = data["email"]
    my_user.password = data["password"]

    #created_user = database["TEST"]["users"].insert_one(my_user.__dict__)
    created_user = database["LABAPI"]["users"].insert_one(my_user.__dict__)

    #print(created_user.inserted_id)

    return jsonify({'id': str(created_user.inserted_id)})

#@user.route("/v0/users/", methods=["GET"])
@user.route("/v1/users/", methods=["GET"])

def fetch():
    data = json.loads(request.data)
    print(data)

    #result = database["TEST"]["users"].find_one({"_id": ObjectId(data["id"])})
    result = database["LABAPI"]["users"].find_one({"_id": ObjectId(data["id"])})

    print(result)

    return jsonify({"id": str(result["_id"]), "name": result["name"], "email": result["email"]})