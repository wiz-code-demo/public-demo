from datetime import datetime

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def show_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Time</h1><p>{current_time}</p>"


@app.route("/direct_inject", methods=["GET"])
def direct_inject():
    exec_param = request.args.get("exec")
    exec("%s" % exec_param)


if __name__ == '__main__':
    app.run()
