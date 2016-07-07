import os
from filecmp import cmp
import pytest
from src.files import save_to_temp_file, create_zip_from_files, create_zip_from_data

TEST_FILE = 'files/Resume.pdf'
OUTPUT_PATH = '/tmp/'
OUTPUT_FILE_NAME = 'resume.pdf'
OUTPUT_ZIP_NAME = 'archive.zip'
OUTPUT_FILE = OUTPUT_PATH + OUTPUT_FILE_NAME
OUTPUT_ZIP = OUTPUT_PATH + OUTPUT_ZIP_NAME


def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)


@pytest.yield_fixture(autouse=True)
def before_each():
    delete_file(OUTPUT_FILE)
    delete_file(OUTPUT_ZIP)
    yield


def test_save_to_temp_file():
    with open(TEST_FILE, "rb") as input_file:
        data = input_file.read()
        save_to_temp_file(data, OUTPUT_FILE_NAME)
    assert os.path.isfile(OUTPUT_FILE)
    assert cmp(TEST_FILE, OUTPUT_FILE)


def test_create_zip_from_files():
    create_zip_from_files([TEST_FILE], OUTPUT_ZIP_NAME)
    assert os.path.isfile(OUTPUT_ZIP)


def test_create_zip_from_data():
    with open(TEST_FILE, "rb") as input_file:
        data = input_file.read()
        create_zip_from_data([data], 'pdf', OUTPUT_ZIP_NAME)
    assert os.path.isfile(OUTPUT_ZIP)
