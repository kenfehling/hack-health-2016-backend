from collections import OrderedDict


def only_fields(record, fields):
    d = OrderedDict()
    for field in fields:
        d[field] = record[field]
    return d


def only_fields_for_all(records, fields):
    return [only_fields(record, fields) for record in records]
