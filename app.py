from flask import Flask
import socket
import datetime
app = Flask(__name__)

@app.route('/')
def hello():
        return f"Served by {socket.gethostname()} | {datetime.datetime.now()}"

if __name__ == "__main__":
        app.run(host = "0.0.0.0", port=8000)