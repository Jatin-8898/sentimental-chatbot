from flask import Flask, jsonify,request, make_response
import requests
app = Flask(__name__)

emojis ={
    "pos" : ":)",
    "neutral" : ":|",
    "neg" : ":(",
}

@app.route('/', methods=['GET'])
def index():
    return jsonify({"name": "JV"})


@app.route('/respond', methods=['POST'])
def respond_post():
    res = results(request.get_json(force=True)) #Get the json from dialogflow

    #if(res['queryResult']['intent']['displayName'] == 'Sentiment'):
    print(jsonify(res))                 # To convert into json
    return make_response(jsonify(res))


def results(request):
    action = request.get('queryResult')
    params = action['parameters']

    language = params["language"]
    query = params["text"]

    results = fetch_results(query=query, lang=language)
    response = {'fulfillmentText': results}
    return response

def fetch_results(query, lang):
    available_languages = ["english","french", "dutch"]

    if lang.lower() not in available_languages:
        return "Sorrry"+ lang + "language not supported as of now "+ emojis["neg"]
    else:
        lang = lang.lower()    

    url = 'http://text-processing.com/api/sentiment/'
    payload = {"text": query, "language": lang}
    response = requests.post(url, data=payload)

    print(response)
    if response.status_code == 200:
        json_response = response.json()
        label = json_response["label"]
        probability = json_response["probability"][label]
        emoji = emojis[label]

        result = query + " is " + label + " " + emoji + " with " + str(int (probability*100)) + "%"
    else:
        result = "request exceed the limit" 

    return result      

if(__name__ == "__main__"):
    app.run(port=8080, debug=True)
