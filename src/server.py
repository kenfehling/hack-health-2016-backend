from flask import Flask, request
from flask.ext.cors import CORS, cross_origin
from src.db import save_record

ALLOWED_EXTENSIONS = {'txt', 'pdf'}
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


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run()
