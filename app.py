from flask import Flask
import logging


logging.basicConfig(filename="app.log", level=logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("%s endpoint was reached", "/")
    return "Hello World!"


@app.route("/status")
def status():
    app.logger.info("%s endpoint was reached", "/status")
    return {"result": "OK - healthy"}, 200


@app.route("/metrics")
def metrics():
    app.logger.info("%s endpoint was reached", "/metrics")
    return {
        "status": "success",
        "code": 0,
        "data": {"UserCount": 140, "UserCountActive": 23},
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
