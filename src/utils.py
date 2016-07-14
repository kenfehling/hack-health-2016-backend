from collections import OrderedDict
from config import FIELDS


def record_with_only_form_fields(record):
    d = OrderedDict()
    for field in FIELDS:
        d[field] = record[field]
    return d


def records_with_only_form_fields(records):
    return [record_with_only_form_fields(record) for record in records]


def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions
