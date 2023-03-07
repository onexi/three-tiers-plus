# imports
from flask import Flask, render_template, request, redirect, jsonify

# web application
app = Flask(__name__)


# ---------------
#    YOUR CODE
# ---------------


# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)


# query string sample
# curl 'localhost:3000/viewer?username=alex'

# post using curl
# curl --data "first=peter&last=parker" localhost:3000/viewer

