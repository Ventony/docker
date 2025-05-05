from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def call_api():
    try:
        res = requests.get("http://api:5001/")
        return f"API 응답: {res.text}"
    except Exception as e:
        return f"에러: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
