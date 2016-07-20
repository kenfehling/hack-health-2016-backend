import requests
from jinja2 import Environment, PackageLoader
from src.config import MAILGUN_API_KEY, MAILGUN_DOMAIN

env = Environment(loader=PackageLoader(__name__, 'templates'))
template = env.get_template('email.html')


def send_email(to, subject, context):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages" % MAILGUN_DOMAIN,
        auth=("api", MAILGUN_API_KEY),
        data={"from": "WiCS (Women in Computer Science) <mailgun@%s>" % MAILGUN_DOMAIN,
              "to": to,
              "subject": subject,
              "html": template.render(**context)})
