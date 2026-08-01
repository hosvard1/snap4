from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


BOT_TOKEN = "8753863153:AAESoe2pWFsz_bEteF_hFZVM0l9tfwM61ZE"
CHAT_ID = "1584744130"

@app.route("/send", methods=["POST"])
def send():

    data = request.json

    print(data) 

    message = f"""
Test message

Username: {data['username']}
Password length: {data['passwordLength']}
"""


    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


    r = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })


    print(r.text)  # Telegram-ի պատասխանը


    return jsonify({
        "status":"ok"
    })


if __name__ == "__main__":
    app.run(port=5000)