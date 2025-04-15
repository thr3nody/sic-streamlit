import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)
client = genai.Client(api_key=os.getenv("GEMINI_API"))


@app.route("/hello")
def entry_point():
    return "Hi babe."


@app.route("/environment", methods=["POST"])
def post_environment():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400
    prompt = (
        "Rephrase the following gas sensor readings into clear, "
        "natural language:\n\n" + str(data)
    )
    resp = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return jsonify({"text": resp.text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
