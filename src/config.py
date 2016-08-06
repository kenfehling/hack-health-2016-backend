from os.path import join, dirname
from dotenv import load_dotenv  # python-dotenv
import os

dotenv_path = join(dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

FIELDS = [
    'name',
    'email',
    'gender',
    'year',
    'tshirt',
    'diet',
    'first_hackathon',
    'num_hackathons',
    'theme',
    'idea',
    'other'
]

MAILGUN_API_KEY = os.environ['MAILGUN_API_KEY']
MAILGUN_DOMAIN = os.environ['MAILGUN_DOMAIN']
MAILGUN_PUBLIC_KEY = os.environ['MAILGUN_PUBLIC_KEY']
MAILGUN_SMTP_LOGIN = os.environ['MAILGUN_SMTP_LOGIN']
MAILGUN_SMTP_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
MAILGUN_SMTP_PORT = os.environ['MAILGUN_SMTP_PORT']
MAILGUN_SMTP_SERVER = os.environ['MAILGUN_SMTP_SERVER']

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

NOTE = 'The resume filenames contain the row numbers in the spreadsheet\n(Shan_Liu-2.pdf is the resume for row 2, etc.)'
