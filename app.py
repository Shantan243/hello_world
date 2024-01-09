from flask import Flask, request
import json

# Initializing flask app
app = Flask(__name__)



# Controller-1
@app.route("/demo", methods=['GET'])
def get_demo():
    return "This is a demo api"


# Controller-2
@app.route("/name", methods=['POST'])
def get_demo_name():
    data = request.data
    body = json.loads(data)
    name = body["name"]
    return "Hello, I am {}!".format(name)


# Running the api
if __name__ == '__main__':
    app.run()
