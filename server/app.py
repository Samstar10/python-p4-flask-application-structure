#!/usr/bin/env python3

from flask import Flask
# from werkzeug.utils import url_quote

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

@app.route('/<string:username>')
def user(username):
    profile = f'<h1>Profile for {username}</h1>'
    return profile


if __name__ == '__main__':
    app.run(port=5555)