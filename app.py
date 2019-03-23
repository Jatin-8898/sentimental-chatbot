from flask import Flask, jsonify,request

app = Flask(__name__)


@app.route('/respond', methods=['GET'])
def respond():
    return jsonify({"name": "JV"})


@app.route('/respond', methods=['POST'])
def respond_post():
    return request.data


if(__name__ == "__main__"):
    app.run(port=8080, debug=True)
