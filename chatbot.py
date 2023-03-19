from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set the OpenAI API key using the OPENAI_API_KEY environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Get the input message from the request
    message = request.json["message"]

    # Use OpenAI to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Q: {message}\nA:",
        temperature=0.5,
        max_tokens=1024,
        n = 1,
        stop = "\n"
    )

    # Extract the first answer from the response
    answer = response.choices[0].text.strip()

    # Return the answer as a JSON object
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
