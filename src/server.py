from flask import Flask, request

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def hello_world():
    name = request.form['name']
    email = request.form['email']
    resume = request.form['resume']


if __name__ == '__main__':
    app.run()
