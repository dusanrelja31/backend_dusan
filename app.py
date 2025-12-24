from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from markupsafe import escape

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    response = jsonify(name="You are welcome! I'm Server")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response