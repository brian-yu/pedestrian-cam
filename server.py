from flask import Flask, url_for, send_from_directory, send_file
app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    return "hello!"

@app.route('/predictions')
def get_predictions():
    return send_file('predictions.png', mimetype='image/png')

@app.route('/cam')
def get_cam():
    return send_file('cam.png', mimetype='image/png')

@app.route('/log')
def get_log():
    return send_file('bar.txt')

@app.route('/bar')
def get_bar():
    return send_file('bar.txt')

@app.route('/restaurant')
def get_restaurant():
    return send_file('restaurant.txt')

if __name__ == "__main__":
    app.run()