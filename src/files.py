import os
import csv
from zipfile import ZipFile
from src.config import OUTPUT_FIELDS


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


def save_to_temp_files(data_list, extension, folder='', filenames=None):
    filenames = filenames if filenames is not None else range(1, len(data_list) + 1)
    return [save_to_temp_file(data, '%s.%s' % (filenames[i], extension), folder) for i, data in enumerate(data_list)]


def create_temp_zip_from_files(files, filename):
    with ZipFile('/tmp/' + filename, 'w') as z:
        for file in files:
            z.write(file)


def create_temp_zip_from_data(data_list, extension, filename, folder=''):
    files = save_to_temp_files(data_list, extension, folder)
    return create_temp_zip_from_files(files, filename)


def create_temp_csv(data, filename):
    file = '/tmp/' + filename
    with open(file, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(OUTPUT_FIELDS)
        for row in data:
            csv_writer.writerow(row.values())
    return file


def create_temp_txt(text, filename):
    file = '/tmp/' + filename
    with open(file, 'w') as f:
        f.write(text)
    return file
