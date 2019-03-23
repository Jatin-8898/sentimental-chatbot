from flask import Flask, jsonify,request, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({"name": "JV"})


@app.route('/respond', methods=['POST'])
def respond_post():
    res = (request.get_json(force=True)) #Get the json from dialogflow

    if(res['queryResult']['intent']['displayName'] == 'Sentiment'):
        print(jsonify(res))                 # To convert into json
        return make_response(jsonify({"fulfillmentText":"THE INTENT MATCHES"}))

if(__name__ == "__main__"):
    app.run(port=8080, debug=True)
