import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)
client = genai.Client(api_key=os.getenv("GEMINI_API"))

latest_data = {}


@app.route("/hello")
def entry_point():
    return "Hi babe."


@app.route("/environment", methods=["POST"])
def post_environment():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400
    prompt = (
        "Rephrase the following gas sensor readings into clear and fun natural language in less than a paraphraph, also describe where these gases might came from, then give safety suggestion to reduce health risk in such condition:\n\n"
        + str(data)
    )
    resp = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return jsonify({"text": resp.text})


@app.route("/latest-data", methods=["POST"])
def post_latest_data():
    global latest_data
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}, 400)
    latest_data = data
    return jsonify({"message": "latest_data updated successfully"}), 200


@app.route("/latest-data", methods=["GET"])
def get_latest_data():
    return jsonify(latest_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
