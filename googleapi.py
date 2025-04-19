import google.generativeai as palm

def configure_api(api_key):
    palm.configure(api_key=api_key)

def list_models():
    models = palm.list_models()
    for model in models:
        print(model.name)

def generate_response(prompt):
    try:
        completion = palm.generate_text(
            model="models/text-bison-001", 
            prompt=prompt,
            temperature=0.99,  #Controls the randomness of the output. A higher temperature (closer to 1) results in more random outputs, while a lower temperature (closer to 0) results in more deterministic outputs.
            max_output_tokens=800,
        )
        return completion.result
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

def chatbot():
    print("Welcome to Yago Assistant!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = generate_response(f"You are a helpful assistant. Your name is Yago Assistant. {user_input}")
        if response:
            print(f"Yago Assistant: {response}")

if __name__ == "__main__":
    api_key = "enter your api key" 
    configure_api(api_key)
    list_models() 
    chatbot()