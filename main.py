from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "SaintlyStrive backend is running!"

@app.route("/generate_reflection", methods=["POST"])
def generate_reflection():
    data = request.json
    verse = data.get("verse", "Be still and know that I am God. - Psalm 46:10")

    prompt = f"Give a short 2-sentence Catholic reflection for the verse: {verse}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    reflection = response['choices'][0]['message']['content']
    return jsonify({"reflection": reflection})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
