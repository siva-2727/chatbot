from flask import Flask, request, jsonify, render_template
import google.generativeai as palm

app = Flask(__name__)

def configure_api(api_key):
    palm.configure(api_key=api_key)

def generate_response(prompt):
    try:
        completion = palm.generate_text(
            model="models/text-bison-001", 
            prompt=prompt,
            temperature=0.99, 
            max_output_tokens=800,
        )
        return completion.result
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    response = generate_response(f"You are a helpful assistant. Your name is Yago Assistant. {user_input}")
    return jsonify({"response": response})

if __name__ == "__main__":
    api_key = "enter your api key"  
    configure_api(api_key)
    app.run(debug=True)
