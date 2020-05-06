import flask
from flask import request, jsonify

app=flask.Flask(__name__)
app.config["DEBUG"]=True


@app.route('/',methods=['GET'])
def home():
    return "DATASET"

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    #json is formatted as list, so we choose 1st element from list
    url_n1 = req_data 
    return '''
           The 1st url is: {}
           '''.format(url_n1) 


app.run()
