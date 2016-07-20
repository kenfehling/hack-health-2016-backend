import requests
from src.config import MAILGUN_API_KEY, MAILGUN_DOMAIN, MAILGUN_PUBLIC_KEY, MAILGUN_SMTP_LOGIN, MAILGUN_SMTP_PASSWORD, MAILGUN_SMTP_PORT, MAILGUN_SMTP_SERVER


def send_email(to, subject, body):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages" % MAILGUN_DOMAIN,
        auth=("api", MAILGUN_API_KEY),
        data={"from": "WiCS (Women in Computer Science) <mailgun@%s>" % MAILGUN_DOMAIN,
              "to": to,
              "subject": subject,
              "text": body})
