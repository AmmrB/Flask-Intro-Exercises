from flask import Flask

app = Flask(__name__)

@app.route('/Hello!')
def index():
    return 'Hello!'

@app.route('/hello/world')
def hello_world():
    return 'Hello World!'

@app.route('/hello/people')
def hello_people():
    return 'Hello People!'