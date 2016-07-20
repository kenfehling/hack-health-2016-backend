from src.mail import send_email


def test_send_email():
    send_email('ken@androidideas.org', 'Test', 'Hello World')
