from flask import Flask, jsonify, request
from pprint import pprint
app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    result = f"Hello {name}"
   
    return result


@app.route("/operate/<n1>/<n2>")
def operate(n1, n2):
    return f"{n1} + {n2} = {n1 + n2}"


@app.route("/add/<int:n1>/<int:n2>")
def add(n1, n2):
    return f"{n1} + {n2} = {n1 + n2}"


@app.route("/mirror")
def mirror():
    rq_vars = vars(request)
    pprint(rq_vars)
    return jsonify(request.json)