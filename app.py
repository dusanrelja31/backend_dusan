from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    response = jsonify(name="You are welcome! I'm Server")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    # Run the app on port 8000
    app.run(port=8000)