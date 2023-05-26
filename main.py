from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/webhooks", methods=["GET, POST"])
def webhooks():
	return f"data:{request.args.get("data")}"

@app.route("/", methods=["GET, POST"])
def start():
	return f"{request.args.get("data")}"

@app.route("/facebook", methods=["GET, POST"])
def facebook():
	return f"{request.args.get("data")}"

if __name__ == "__main__":
	app.run()
