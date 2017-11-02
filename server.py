from flask import Flask, url_for
app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    return app.send_static_file('predictions.png')