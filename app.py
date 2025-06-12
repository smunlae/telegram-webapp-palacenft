from flask import Flask, request, render_template
import requests
import os
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fetch_offers", methods=["POST"])
def fetch_offers():
    payload = request.get_json()

    # Извлекаем нужные поля
    user_data = payload.get("user", {})
    auth_date = payload.get("auth_date", "")
    signature = payload.get("signature", "")
    hash_ = payload.get("hash", "")

    # Преобразуем весь payload в JSON-строку
    full_user_data = json.dumps(payload)

    headers = {
        "x-user-data": full_user_data,
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": "https://palacenft.com/collection/2",
        "auth_date": str(auth_date),
        "signature": signature,
        "hash": hash_
    }

    try:
        resp = requests.get(
            "https://palacenft.com/api/v1/markets/offers",
            headers=headers,
            params={
                "collection_id": "2",
                "limit": "40",
                "offset": "0",
                "sort": "price_asc"
            }
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
