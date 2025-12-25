from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = jsonify(name="You are welcome! I'm Server.")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host="0.0.0.0",port=5000)