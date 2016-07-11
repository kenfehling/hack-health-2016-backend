from flask import Flask, request, render_template, send_from_directory
from flask.ext.cors import CORS, cross_origin
from config import FIELDS
from files import save_to_temp_file, create_temp_csv, save_to_temp_files, create_temp_zip_from_files
from src.db import save_record, get_records, get_record
from utils import records_with_only_form_fields

ALLOWED_EXTENSIONS = {'pdf'}
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    resume = request.files['resume']
    if resume and allowed_file(resume.filename):
        save_record(request.form, resume)

    return 'OK'  # {"success": True}


@app.route("/")
def home():
    return render_template('index.html', title="Home", responses=get_records(), fields=FIELDS)


@app.route("/response/<id>/resume")
def resume(id):
    resume = get_record(id)['resume']
    save_to_temp_file(resume, 'resume.pdf')
    return send_from_directory('/tmp', 'resume.pdf')


@app.route("/archive")
def archive():
    records = get_records()
    resumes = [record['resume'] for record in records]
    data = records_with_only_form_fields(records)
    csv = create_temp_csv(data, 'spreadsheet.csv')
    resume_files = save_to_temp_files(resumes, 'pdf', folder='resumes/')
    create_temp_zip_from_files(resume_files + [csv], 'archive.zip')
    return send_from_directory('/tmp', 'archive.zip')


@app.route('/pixel.gif')
def pixel():
    return app.send_static_file('pixel.gif')


if __name__ == '__main__':
    app.run()
