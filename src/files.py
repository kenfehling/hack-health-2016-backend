from zipfile import ZipFile


def save_to_temp_file(data, filename):
    file = '/tmp/' + filename
    f = open(file, "wb")
    f.write(data)
    f.close()
    return file


def create_zip_from_files(files, filename='archive.zip'):
    with ZipFile('/tmp/' + filename, 'w') as z:
        for file in files:
            z.write(file)


def create_zip_from_data(data_list, extension, filename='archive.zip'):
    files = [save_to_temp_file(data, '%d.%s' % (i, extension)) for i, data in enumerate(data_list)]
    return create_zip_from_files(files, filename)
