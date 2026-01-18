import os
from flask import Flask, request, jsonify
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# AGENT_INSTRUCTION="You are Bob, a Python wizard capable of building the most advanced AI Agents.  Say 'hi' and introduce yourself"
AGENT_INSTRUCTION="You are Tony, a Black Belt Product Manager capable of building the most advanced Digital Products.  Say 'hi' and introduce yourself"

print("A: Flask", flush=True)
app = Flask(__name__)
print("B: Flask", flush=True)

# Initialize the Azure OpenAI Client
print("A: AzureOpenAI", flush=True)
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)
print("B: AzureOpenAI", flush=True)

@app.route("/")
def home():
    return "Server is running! Use the /chat endpoint for AI."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Call Azure OpenAI
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            messages=[
                {"role": "system", "content": os.getenv("AGENT_INSTRUCTION")},
                {"role": "user", "content": user_input}
            ]
        )

        # Extract the assistant's reply
        answer = response.choices[0].message.content
        return jsonify({"reply": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)