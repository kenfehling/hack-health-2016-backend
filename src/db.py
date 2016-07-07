import os
from bson import ObjectId
from pymongo import MongoClient
from bson.binary import Binary


def get_mongo_uri():
    if 'MONGODB_URI' in os.environ:
        return os.environ['MONGODB_URI']
    else:
        return 'mongodb://localhost:27017/'

client = MongoClient(get_mongo_uri())
db = client.test


def save_record(name, email, resume):
    data = {
        'name': name,
        'email': email,
        'resume': Binary(resume.read())
    }
    db.responses.insert_one(data)


def get_records():
    return [doc for doc in db.responses.find()]


def get_record(id):
    return db.responses.find_one({'_id': ObjectId(id)})
