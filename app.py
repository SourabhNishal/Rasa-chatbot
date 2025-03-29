from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message})
    bot_message = response.json()
    return jsonify(bot_message)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
 
