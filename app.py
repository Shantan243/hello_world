import os

from flask import Flask
app = Flask(__name__)
@app.route('/hello_world/<name>')
 
def hello_world(name):
    return "Hello " + name
if __name__ == '__main__':
    app.run(debug=True)