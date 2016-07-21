import os
from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
from utils import get_only_form_fields


def get_mongo_uri():
    if 'MONGODB_URI' in os.environ:
        return os.environ['MONGODB_URI']
    else:
        return 'mongodb://localhost:27017/'

client = MongoClient(get_mongo_uri())
db = client.heroku_lwc4tt1r


def get_records():
    return [doc for doc in db.responses.find()]


def get_record(id):
    return db.responses.find_one({'_id': ObjectId(id)})


def get_record_by_email(email):
    return db.responses.find_one({'email': email})


def check_email_exists(email):
    return get_record_by_email(email) is not None


def save_record(form_data, resume, success_fn, failure_fn):
    data = get_only_form_fields(form_data)
    if check_email_exists(data['email']):
        return failure_fn("Hey, you're already signed up")
    else:
        data['resume'] = Binary(resume.read())
        db.responses.insert_one(data)
        return success_fn(form_data)
