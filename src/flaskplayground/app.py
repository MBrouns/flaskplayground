from flask import Flask, jsonify, request, abort
from pprint import pprint
import os
import redis


app = Flask(__name__)
r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "localhost"), 
    port=6379, 
    db=0, 
    decode_responses=True
)
REDIS_NAMES_KEY = "names"



@app.route('/names')
def list_names():
    names = r.smembers(REDIS_NAMES_KEY)
    return {"names": list(names)}


@app.route('/names/<name>', methods=["GET"])
def get_name(name):
    if not r.sismember(REDIS_NAMES_KEY, name):
        abort(404)
        
    return f"hello {name}!"    
    
    
@app.route('/names/<name>', methods=["POST"])
def post_name(name):
    new = r.sadd(REDIS_NAMES_KEY, name)
    
    if not new:
        return "already exists", 208

    return "ok", 201