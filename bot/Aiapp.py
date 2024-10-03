#by back4app 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Only for debugging while developing
    app.run(host='0.0.0.0', port=8000, debug=True)
