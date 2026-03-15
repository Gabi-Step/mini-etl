from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/todo/<int:todo_ID>', methods = ['GET'])
def get(todo_ID):
    ...
