import os
from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
app.config['SECRET'] = "bruh"
sock = Sock(app)


@app.route("/")
def hello():
    return "Hello Bois!"


@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send(data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)