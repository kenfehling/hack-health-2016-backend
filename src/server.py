from flask import Flask, request
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)


@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    #name = request.form['name']
    #email = request.form['email']
    #resume = request.form['resume']
    return 'OK' #{"success": True}


if __name__ == '__main__':
    app.run()
