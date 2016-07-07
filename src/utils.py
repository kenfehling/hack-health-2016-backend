from collections import OrderedDict
from config import FIELDS


def record_without_resume(record):
    d = OrderedDict()
    for field in FIELDS:
        d[field] = record[field]
    return d


def records_without_resumes(records):
    return [record_without_resume(record) for record in records]
