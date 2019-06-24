from flask import Flask, request
app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    return int(request.json['x']) + int(request.json['y'])
