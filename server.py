import os
from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS

# take environment variables from .env
load_dotenv()  

app = Flask(__name__)

# Enable CORS for all routes and allow credentials
# This will enable the frontend to make requests to the backend. 
# My current frontend is running on http://localhost:5173 but you should change it to your frontend URL.
CORS(app, resources={r"/*/*": {"origins": "http://localhost:5173"}})

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("LLM_ENDPOINT")
)

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        input_message = data["prompt"]

        # Create chat completion
        response = client.chat.completions.create(
            model=os.environ.get("MODEL"),
            messages=[
                {"role": "system", "content": "You are an AI chatbot who specializes in giving daily advice on sports."},
                {"role": "user", "content": input_message}
            ]
        )

        output = response.choices[0].message.content
        return jsonify({"output": output})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
