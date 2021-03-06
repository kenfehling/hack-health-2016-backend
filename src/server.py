from functools import wraps
from flask import Flask, request, Response, render_template, send_from_directory, jsonify
from flask.ext.cors import CORS, cross_origin
from config import OUTPUT_FIELDS, USERNAME, PASSWORD, NOTE
from files import save_to_temp_file, create_temp_csv, save_to_temp_files, create_temp_zip_from_files, create_temp_txt
from mail import send_email
from src.db import save_record, get_records, get_record
from utils import only_fields_for_all

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['DEBUG'] = True


def check_auth(username, password):
    return username == USERNAME and password == PASSWORD


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    def success_fn(data):
        send_email(data['email'], {'name': data['name']})
        return jsonify(**{"success": True})

    def failure_fn(error):
        return jsonify(**{"success": False, "error": error})

    responses = request.form.copy()
    responses['diet'] = [d for d in request.form.getlist('diet') if d]  # Get list of all dietary restrictions given
    resume = request.files['resume'] if 'resume' in request.files else None
    return save_record(responses, resume, success_fn=success_fn, failure_fn=failure_fn)


@app.route("/")
@requires_auth
def home():
    records = get_records()
    emails = ','.join(set([r['email'] for r in records]))
    return render_template('index.html', title="Home", responses=records, fields=OUTPUT_FIELDS, emails=emails)


@app.route("/response/<id>/resume")
@requires_auth
def resume(id):
    resume = get_record(id)['resume']
    save_to_temp_file(resume, 'resume.pdf')
    return send_from_directory('/tmp', 'resume.pdf')


@app.route("/archive")
@requires_auth
def archive():
    records = get_records()
    resumes = [r['resume'] for r in records if 'resume' in r]
    resume_names = ["%s-%i" % (r['name'].replace(' ', '_'), i + 2) for i, r in enumerate(records) if 'resume' in r]
    data = only_fields_for_all(records, fields=OUTPUT_FIELDS)
    csv = create_temp_csv(data, 'spreadsheet.csv')
    resume_files = save_to_temp_files(resumes, 'pdf', folder='resumes/', filenames=resume_names)
    readme = create_temp_txt(NOTE, 'README.txt')
    create_temp_zip_from_files(resume_files + [csv] + [readme], 'archive.zip')
    return send_from_directory('/tmp', 'archive.zip')


@app.route("/response/<id>", methods=['DELETE'])
@requires_auth
def delete(id):
    return 'Not implemented'


# Loading this image will wake up Heroku from the frontend site so it's ready
@app.route('/pixel.gif')
def pixel():
    return app.send_static_file('pixel.gif')


if __name__ == '__main__':
    app.run()
