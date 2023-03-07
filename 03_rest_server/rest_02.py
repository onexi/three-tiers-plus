# import package
from flask import Flask, jsonify, request

# create application instance
app = Flask(__name__)

# root route - landing page
@app.route('/', methods=['GET','POST'])
def hello_world():
    if (request.method == 'POST'):
        someJson = request.get_json()
        return jsonify({'yourData': someJson}), 201
    else:
        return jsonify({'message': 'Hello, World!'})

@app.route('/timesTen/<int:num>', methods=['GET'])
def timesTen(num):
    return jsonify({'result': num*10});

# start server - note the port is 3000
if __name__ == '__main__':
    app.run(debug=True, port=3000)

# ------------------------------------------------------------
# invoke using get:
# curl http://127.0.0.1:3000
# 
# invoke using post:
# curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:3000/
# 
# invoke x10:
# curl http://127.0.0.1:3000/timesTen/10
# ------------------------------------------------------------