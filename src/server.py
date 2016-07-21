from flask import Flask, request, render_template, send_from_directory, jsonify
from flask.ext.cors import CORS, cross_origin
from config import FIELDS, ALLOWED_RESUME_EXTENSIONS
from files import save_to_temp_file, create_temp_csv, save_to_temp_files, create_temp_zip_from_files
from mail import send_email
from src.db import save_record, get_records, get_record
from utils import get_only_form_fields_for_all, allowed_file

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/register', methods=['POST'])
@cross_origin()
def register():

    def success_fn(data):
        send_email(data['email'], {'name': data['name']})
        return jsonify(**{"success": True})

    def failure_fn(error):
        return jsonify(**{"success": False, "error": error})

    resume = request.files['resume']
    if resume and allowed_file(resume.filename, ALLOWED_RESUME_EXTENSIONS):
        return save_record(request.form, resume, success_fn=success_fn, failure_fn=failure_fn)
    else:
        return failure_fn("Please upload a resume in %s format" % '/'.join(ALLOWED_RESUME_EXTENSIONS))


@app.route("/")
def home():
    records = get_records()
    emails = ','.join(set([r['email'] for r in records]))
    return render_template('index.html', title="Home", responses=records, fields=FIELDS, emails=emails)


@app.route("/response/<id>/resume")
def resume(id):
    resume = get_record(id)['resume']
    save_to_temp_file(resume, 'resume.pdf')
    return send_from_directory('/tmp', 'resume.pdf')


@app.route("/archive")
def archive():
    records = get_records()
    resumes = [record['resume'] for record in records]
    data = get_only_form_fields_for_all(records)
    csv = create_temp_csv(data, 'spreadsheet.csv')
    resume_files = save_to_temp_files(resumes, 'pdf', folder='resumes/')
    create_temp_zip_from_files(resume_files + [csv], 'archive.zip')
    return send_from_directory('/tmp', 'archive.zip')


# Loading this image will wake up Heroku from the frontend site so it's ready
@app.route('/pixel.gif')
def pixel():
    return app.send_static_file('pixel.gif')


if __name__ == '__main__':
    app.run()
