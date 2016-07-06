from flask import Flask, request

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def hello_world():
    name = request.form['name']
    email = request.form['email']
    resume = request.form['resume']
    return {"success": True}


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run()
