from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return url_for('static', filename='predictions.png')