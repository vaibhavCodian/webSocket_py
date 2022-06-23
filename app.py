import os
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__, template_folder='client')
app.config['SECRET'] = "bruh"
sock = Sock(app)

connected = set()

@app.route("/")
def hello():
    return render_template("index.html")


@sock.route('/echo')
def echo(ws):
    connected.add(ws)
    while True:
        data = ws.receive()
        for conn in connected:
            if conn != ws:
                conn.send(data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
