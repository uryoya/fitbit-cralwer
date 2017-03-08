"""FitbitでOAuth認証をするための簡易Webアプリ."""
import base64
import pickle
import os
import requests

from urllib.parse import urlencode
from flask import Flask, redirect, request, jsonify, render_template


app = Flask(__name__)
app.config.from_pyfile('./authorizer.cfg')
AUTHORIZATION_URL = app.config['AUTHORIZATION_URL']
ACCESS_TOKEN_URL = app.config['ACCESS_TOKEN_URL']
CLIENT_SECRET = app.config['CLIENT_SECRET']
CLIENT_ID = app.config['CLIENT_ID']


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
