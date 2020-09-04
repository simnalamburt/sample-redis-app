from redis import Redis
from flask import Flask, render_template, request, jsonify

db = Redis(port=29597)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/counter', methods = ['GET', 'PUT'])
def get():
    if request.method == 'GET':
        counter = db.get('counter')
        if counter is None:
            counter = b'0'
        return jsonify(int(counter))

    elif request.method == 'PUT':
        counter = request.get_json()
        db.set('counter', counter)
        return '', 204
