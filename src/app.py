from flask import Flask
from config import DEBUG, PORT

app = Flask(__name__)

@app.route('/')
def index():
    return "hola mundo"

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)