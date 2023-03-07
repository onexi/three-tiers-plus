# import package
from flask import Flask

# create application instance
app = Flask(__name__)

# root route - landing page
@app.route('/')
def hello_world():
    return 'Hello, World!'

# start server - note the port is 3000
if __name__ == '__main__':
    app.run(debug=True, port=3000)

# ------------------------------
# invoke with browser or curl
# http://localhost:3000
# http://127.0.0.1:3000
# ------------------------------