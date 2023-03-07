# -----------------------
# you to install flask
#   pip install Flask
# -----------------------

# imports
from flask import Flask, render_template, request, redirect
import sqlite3

# connect to db and get cursor
connection = sqlite3.connect("data/contacts.db", check_same_thread=False)
cursor = connection.cursor()

# web application
app = Flask(__name__)


# ---------------
#    YOUR CODE
# ---------------

        
# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)