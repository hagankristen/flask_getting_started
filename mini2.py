from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)

@app.route("/name", methods=["GET"])
def name():
    """Creates URL ending in /name with json of name shown

    :returns name1: json version of name
    """
    name1 = {
    "name": "Kristen Hagan"
    }
    return jsonify(name1), 200

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    """Creates URL ending in /hello/<inputname> with hello message

    :param name: takes input of name for hello message
    :returns hi: json version of hello message and name
    """
    hi = {
    "message": "Hello there, %s" %name,
    }
    return jsonify(hi), 200

@app.route("/distance", methods=["POST"])
def distance():
    """POST that calcuates distance between input points

    :param r: requests json of two point inputs
    :returns data: json version of distance between points
                    and point info
    """
    r = request.get_json()
    a =  r["a"]
    b =  r["b"]
    a1 = a[0]
    a2 = a[1]
    b1 = b[0]
    b2 = b[1]
    s = np.sqrt(np.square(b1-a1)+ np.square(b2-a2))
    data = {
            "distance": s,
            "a": a,
            "b": b
            }

    return jsonify(data), 200
