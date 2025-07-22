from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "SaintlyStrive backend is running!"

@app.route("/generate_reflection", methods=["POST"])
def generate_reflection():
    try:
        # Check if API key is available
        if not os.getenv("OPENAI_API_KEY"):
            return jsonify({"error": "OpenAI API key not configured"}), 500
        
        data = request.json
        verse = data.get("verse", "Be still and know that I am God. - Psalm 46:10")

        prompt = f"Give a short 2-sentence Catholic reflection for the verse: {verse}"

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        reflection = response.choices[0].message.content
        return jsonify({"reflection": reflection})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
