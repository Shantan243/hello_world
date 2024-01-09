from flask import Flask, request, jsonify
import json

# Initializing flask app
app = Flask(__name__)



# Controller-1
@app.route("/demo", methods=['GET'])
def get_demo():
    return "This is a demo api"


# Controller-2
@app.route("/name", methods=['GET','POST'])
def get_demo_name():
    if request.method == 'POST':
        data = request.get_json()
        name = data["name"]
        return jsonify(message="Hello, I am {}!".format(name))
    else:
        return jsonify(message="Hello, I am Flask!")


# Running the api
if __name__ == '__main__':
    app.run()
