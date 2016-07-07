from src.db import save_record

TEST_FILE = 'files/Resume.pdf'


def test_save_record():
    with open(TEST_FILE, 'rb') as resume:
        save_record(name='Ken Fehling', email='ken@androidideas.org', resume=resume)


