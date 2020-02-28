from flask import Flask, render_template,request, redirect, url_for,jsonify
import cv2
import sys
import numpy
import os
import json
import speech
#import gesture
app = Flask(__name__)
@app.route('/')
def landing(name=None):
    return render_template('landing.html',name=name)

@app.route('/blind')
def blind():
    return render_template('blind.html')

@app.route('/speech')
def spech():
    control = speech.call()
    print(control)
    with open('control.json', 'w') as fp:
        json.dump(control,fp)
    return jsonify(control)
    #return render_template('blind.html')

@app.route('/deaf')
def deaf():
    return render_template('deaf.html')
@app.route('/mute')
def mute():
    return render_template('mute.html')

@app.route('/crippled')
def crip():
    return render_template('crippled.html')

@app.route('/security')
def parse(name=None):
    import face_recognize
    print("done")
    return render_template('index.html',name=name)

@app.route('/gesture')
def gesture():
    #gs.detect():
    control = gesture.detect()
    print(control)
    with open('control.json', 'w') as fp:
        json.dump(control,fp)
    return jsonify(control)   

@app.route('/api')
def api():
    with open('control.json','r') as fp:
        return jsonify(json.load(fp))

if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0')