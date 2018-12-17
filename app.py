#!flask/bin/python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "testing, testing, 1.2.3...."
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
