from pymongo import MongoClient
from bson import BSON
from bson.binary import Binary, UUIDLegacy, STANDARD
from bson.codec_options import CodecOptions
from werkzeug.utils import secure_filename

client = MongoClient('mongodb://localhost:27017/')
db = client.test


def save_record(name, email, resume):
    #resume_filename = secure_filename(resume.filename)
    data = {
        'name': name,
        'email': email,
        'resume': Binary(resume.read())
    }
    db.responses.insert_one(data)


def get_records():
    return [doc for doc in db.responses.find()]
