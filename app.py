from flask import Flask, request, render_template, jsonify
import requests
from config import OPENROUTER_API_KEY  # Import API key from config

app = Flask(__name__)

# OpenRouter API request function
def query_llm(prompt):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = query_llm(prompt)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
