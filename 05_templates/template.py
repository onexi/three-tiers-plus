# imports
from flask import Flask, render_template

# web application
app = Flask(__name__)


# ---------------
#    YOUR CODE
# ---------------


# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)