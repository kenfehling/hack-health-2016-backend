from src.db import save_record

TEST_FILE = 'files/Resume.pdf'


def test_save_record():
    form_data = {
        'name': 'Ken Fehling',
        'email': 'ken@androidideas.org',
        'gender': 'Male',
        'year': 'Senior',
        'tshirt': 'L',
        'first_hackathon': 'No',
        'num_hackathons': '3',
        'theme': 'Fitness',
        'idea': 'Not sure'
    }
    with open(TEST_FILE, 'rb') as resume:
        save_record(form_data=form_data, resume=resume)
