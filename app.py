from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Server running"

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": user_input,
            "stream": False
        }
    )

    data = response.json()
    print(data)

    reply = data.get("response", "")
    if reply == "":
        reply = "Loading... try again"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)