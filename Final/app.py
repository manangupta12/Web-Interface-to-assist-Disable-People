from flask import Flask,flash, render_template,request, redirect, url_for,jsonify
import cv2
import sys
import numpy
import os
import json
import speech
import face
import requests

api = "https://us-central1-todo-271522.cloudfunctions.net/api"

#import gesture
app = Flask(__name__)
@app.route('/')
def landing(name=None):
    return render_template('landing.html',name=name)

@app.route('/blind')
def blind():
    return render_template('blind.html')

@app.route('/deaf')
def deaf():
    return render_template('deaf.html')
@app.route('/mute')
def mute():
    return render_template('mute.html')

@app.route('/crippled')
def crip():
    return render_template('crippled.html')

@app.route('/speech')
def spech():
    f = open('control.json')
    data = json.load(f)
    x = speech.call()

    if "fan" in x:
        data["fan"] = x["fan"]
    if "light" in x:
        data["light"] = x["light"]
    if "door" in x:
        data["door"] = x["door"]
    with open('control.json','w') as fp:
        json.dump(data,fp) 
           
    f = open('control.json')
    data = json.load(f)
    x = requests.post(api,data)
    return jsonify(data)

@app.route('/security')
def parse(name=None):
    config = face.detect()
    f = open('control.json')
    data = json.load(f)
    
    data["door"] = config["door"]
    
    with open('control.json','w') as fp:
        json.dump(data,fp)
    f = open('control.json')
    data = json.load(f)
    print(data)
    print(type(data))
    data = json.loads(json.dumps(data))
    x = requests.post(api,data = data)

    return jsonify(data)    

@app.route('/gesture')
def gesture():
    control = gesture.detect()
    print(control)
    with open('control.json', 'w') as fp:
        json.dump(control,fp)
    return jsonify(control)   

# @app.route('/api')
# def api():
#     with open('control.json','r') as fp:
#         return jsonify(json.load(fp))

if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0')
