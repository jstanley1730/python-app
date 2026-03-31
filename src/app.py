# save this as app.py
from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

# details 
@app.route("/api/v1/details")
def details():
    return jsonify(
        {
            'time': datetime.now().isoformat(),
            'hostname': 'localhost'
        }
    )

@app.route("/api/v1/healthz")
def healthz():
    return jsonify(
        {
            'status:': 'up'
        }
    ), 200

@app.route("/api/v1/hostname")
def hostname():
    return jsonify(
        {
            'hostname': socket.gethostname(),
            'message': 'hello from github'
        }
    ), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# '/api/v1/details'
# '/api/v2/healthz'