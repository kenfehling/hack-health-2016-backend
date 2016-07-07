from flask import Flask, request, render_template, send_from_directory
from flask.ext.cors import CORS, cross_origin
from files import save_to_temp_file, create_zip_from_data, create_temp_csv, save_to_temp_files, create_zip_from_files
from src.db import save_record, get_records, get_record
from utils import records_without_resumes

ALLOWED_EXTENSIONS = {'pdf'}
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    name = request.form['name']
    email = request.form['email']
    resume = request.files['resume']
    if name and email and resume and allowed_file(resume.filename):
        save_record(name, email, resume)

    return 'OK' #{"success": True}


@app.route("/")
def home():
    return render_template('index.html', title="Home", responses=get_records())


@app.route("/response/<id>/resume")
def resume(id):
    resume = get_record(id)['resume']
    save_to_temp_file(resume, 'resume.pdf')
    return send_from_directory('/tmp', 'resume.pdf')


@app.route("/archive")
def archive():
    records = get_records()
    resumes = [record['resume'] for record in records]
    data = records_without_resumes(records)
    csv = create_temp_csv(data, 'spreadsheet.csv')
    resume_files = save_to_temp_files(resumes, 'pdf', folder='resumes/')
    create_zip_from_files(resume_files + [csv], 'archive.zip')
    return send_from_directory('/tmp', 'archive.zip')


@app.route('/pixel.gif')
def pixel():
    return app.send_static_file('pixel.gif')


if __name__ == '__main__':
    app.run()
