from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route("/")
def home():
    return "SaintlyStrive backend is running!"

@app.route("/generate_reflection", methods=["POST"])
def generate_reflection():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        verse = data.get("verse", "Be still and know that I am God. - Psalm 46:10")
        prompt = f"Give a short 2-sentence Catholic reflection for the verse: {verse}"

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        reflection = response.choices[0].message['content']
        return jsonify({"reflection": reflection})

    except Exception as e:
        return jsonify({"error": f"Failed to generate reflection: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
