from src.db import save_record

TEST_FILE = 'files/Resume.pdf'


def test_save_record():
    with open(TEST_FILE, 'rb') as resume:
        save_record({
            'name': 'Ken Fehling',
            'email': 'ken@androidideas.org',
            'gender': 'Male',
            'year': 'Senior',
            'tshirt': 'L',
            'first_hackathon': 'No',
            'num_hackathons': '3',
            'theme': 'Fitness',
            'idea': 'Not sure'
        }, resume=resume)

