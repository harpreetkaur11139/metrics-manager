from flask import Flask 
from flask import render_template, request
import json 

app = Flask(__name__)
app.config['SECRET_KEY']='e5ac358c-f0bf-11e5-9e39-d3b532c10a28'


def get_properties():
    """ 
    Reads properties file and return json object of it 
    """
    fle = "properties.json"
    js_file = open(fle)
    json_object = json.load(js_file)
    return json_object


@app.route("/")
def main():
    return "hello!"

@app.route("/harry")
def hello_harry():
    return "Hello from harry"


@app.route("/metrics", methods=["POST"])
def get_metrics():
    json_data = request.json
    print("json data is ", json_data)
    return ""


if __name__ == "__main__":
    app.run(port=5001, debug= True)