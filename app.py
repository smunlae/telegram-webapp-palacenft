from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fetch_offers", methods=["POST"])
def fetch_offers():
    payload = request.get_json()
    init_data = payload.get("init_data", "")

    print("👉 INIT_DATA_RECV:", init_data)

    headers = {
        "x-user-data": init_data,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
        "Referer": "https://palacenft.com/collection/2",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru,en-GB;q=0.8,en-US;q=0.7",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",

        # ⚠️ ЗАМЕНИ НА АКТУАЛЬНЫЕ КУКИ ИЗ DEVTOOLS
        "Cookie": (
            "_ga=GA1.2.2077254862.1749613609; "
            "_ga_E3QPPBEBTS=GS2.1.1749764039.0.5.5g1st1r74064035j6sj0h0; "
            "cf_clearance=mhserNXU6017CpsM.SwinaN358K1W1woTi9FOS0B1PM-1749608626-1.2.11-"
        ),
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
            },
            timeout=10
        )
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error: {http_err.response.status_code}, {http_err.response.text}"}, 401
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
