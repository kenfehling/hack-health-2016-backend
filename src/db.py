import os
from pymongo import MongoClient
from bson import ObjectId
from bson.binary import Binary
from pytz import timezone
from config import INPUT_FIELDS
from utils import only_fields


def get_mongo_uri():
    if 'MONGODB_URI' in os.environ:
        return os.environ['MONGODB_URI']
    else:
        return 'mongodb://localhost:27017/'

client = MongoClient(get_mongo_uri())
db = client.heroku_lwc4tt1r


def get_records():
    records = [doc for doc in db.responses.find().sort('_id')]
    for record in records:
        record['diet'] = ','.join(record['diet'])  # Turn dietary restrictions list into a string with commas
        date = record['_id'].generation_time
        local_date = date.astimezone(timezone('America/New_York'))
        record['date'] = local_date.strftime('%m/%d %H:%M')
    return records


def get_record(id):
    return db.responses.find_one({'_id': ObjectId(id)})


def get_record_by_email(email):
    return db.responses.find_one({'email': email})


def check_email_exists(email):
    return get_record_by_email(email) is not None


def save_record(form_data, resume, success_fn, failure_fn):
    data = only_fields(form_data, INPUT_FIELDS)
    if check_email_exists(data['email']):
        return failure_fn("Hey, you're already signed up")
    else:
        if resume:
            data['resume'] = Binary(resume.read())
        db.responses.insert_one(data)
        return success_fn(form_data)


def delete_record(id):
    db.responses.delete_one({'_id': id})
