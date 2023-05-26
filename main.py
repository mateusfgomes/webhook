from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/facebook", methods=["GET, POST"])
def webhook():
	return f"data:{request.args.get("string")}"
	
if __name__ == "__main__":
	app.run()