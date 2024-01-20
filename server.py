from flask import Flask

app = Flask(__name__)

@app.route('/upload')
def homepage():
    return "Hi there, how ya doin?"
