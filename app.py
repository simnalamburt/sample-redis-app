from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

COUNTER = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/counter', methods = ['GET', 'PUT'])
def get():
    global COUNTER
    if request.method == 'GET':
        return jsonify(COUNTER)
    elif request.method == 'PUT':
        COUNTER = request.get_json()
        return '', 204
