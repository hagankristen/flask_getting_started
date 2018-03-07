from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)

@app.route("/name", methods=["GET"])
def name():
    name1 = {
    "name": "Kristen Hagan"
    }
    return jsonify(name1), 200

@app.route("/hello/<name>", methods=["GET"])
def hello(name):

    hi = {
    "message": "Hello there, %s" %name,
    }
    return jsonify(hi), 200

@app.route("/distance", methods=["POST"])
def distance():

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
