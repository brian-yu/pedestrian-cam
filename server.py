from flask import Flask, url_for, send_from_directory, send_file
app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    return "hello!"

@app.route('/predictions')
def get_image():
    return send_file('predictions.png', mimetype='image/png')

@app.route('/log')
def get_image():
    return send_file('log.txt')

if __name__ == "__main__":
    app.run()