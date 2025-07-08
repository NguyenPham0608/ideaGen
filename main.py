import os
from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS
import json
import time

app = Flask(__name__)
CORS(app)
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)


@app.route("/chat", methods=["POST"])
def analysis():
    message = request.json.get("message")
    try:
        response = client.chat.completions.create(
            model="grok-3",
            messages=[
                {
                    "role": "system",
                    "content": "You are Grok, a highly intelligent, helpful AI assistant.",
                },
                {
                    "role": "user",
                    "content": str(message),
                },
            ],
        )

        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
