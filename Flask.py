from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
    
# novamente não printando nada :c