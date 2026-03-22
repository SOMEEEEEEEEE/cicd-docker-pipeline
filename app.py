from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def hello():
        return f"Hello, CI/CD! | {datetime.datetime.now()}"

if __name__ == "__main__":
        app.run(host = "0.0.0.0", port=8000)