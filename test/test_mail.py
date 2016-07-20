from src.mail import send_email
from flask import Flask

app = Flask(__name__)


def test_send_email():
    send_email('ken@androidideas.org', 'HackHealth registration', {'name': 'Ken Fehling'})
