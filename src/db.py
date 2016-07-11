import os
from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
from utils import record_with_only_form_fields


def get_mongo_uri():
    if 'MONGODB_URI' in os.environ:
        return os.environ['MONGODB_URI']
    else:
        return 'mongodb://localhost:27017/'

client = MongoClient(get_mongo_uri())
db = client.heroku_lwc4tt1r


def save_record(form_data, resume):
    data = record_with_only_form_fields(form_data)
    data['resume'] = Binary(resume.read())
    db.responses.insert_one(data)


def get_records():
    return [doc for doc in db.responses.find()]


def get_record(id):
    return db.responses.find_one({'_id': ObjectId(id)})
