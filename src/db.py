from bson import ObjectId
from pymongo import MongoClient
from bson.binary import Binary

client = MongoClient('mongodb://localhost:27017/')
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
