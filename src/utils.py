from collections import OrderedDict
from config import FIELDS


def only_form_fields(record):
    d = OrderedDict()
    for field in FIELDS:
        d[field] = record[field]
    return d


def only_form_fields_for_all(records):
    return [only_form_fields(record) for record in records]
