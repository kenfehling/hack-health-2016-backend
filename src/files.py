import os
import csv
from zipfile import ZipFile
from src.config import FIELDS


def create_dir(path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))


def save_to_temp_file(data, filename, folder=''):
    dir = '/tmp/' + folder
    create_dir(dir)
    file = dir + filename
    f = open(file, "wb")
    f.write(data)
    f.close()
    return file


def save_to_temp_files(data_list, extension, folder=''):
    return [save_to_temp_file(data, '%d.%s' % (i, extension), folder) for i, data in enumerate(data_list)]


def create_zip_from_files(files, filename):
    with ZipFile('/tmp/' + filename, 'w') as z:
        for file in files:
            z.write(file)


def create_zip_from_data(data_list, extension, filename, folder=''):
    files = save_to_temp_files(data_list, extension, folder)
    return create_zip_from_files(files, filename)


def create_temp_csv(data, filename):
    file = '/tmp/' + filename
    with open(file, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(FIELDS)
        for row in data:
            csv_writer.writerow(row.values())
    return file
