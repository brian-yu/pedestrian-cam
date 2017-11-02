from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('predictions.png')