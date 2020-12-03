from flask import Flask,render_template,request,jsonify , url_for,flash, redirect
import urllib.request




from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer
import os

 
app = Flask(__name__)      


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/thin')
def thin():
  return render_template('thin.html')


if __name__ == '__main__':
  #app.run( debug=True)
  app.run(host='0.0.0.0', port=5000, debug=True)