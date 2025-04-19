import streamlit as st
import google.generativeai as palm

def configure_api(api_key):
    palm.configure(api_key=api_key)

def list_models():
    models = palm.list_models()
    for model in models:
        st.write(model.name)

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
        st.error(f"Error generating response: {e}")
        return None

def chatbot():
    st.title("Yago Assistant")
    st.write("Welcome to Yago Assistant! Type your message below")
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    user_input = st.text_input("You:", key="input")

    if user_input:
        response = generate_response(f"You are a helpful assistant. Your name is Yago Assistant. {user_input}")
        if response:
            st.session_state.conversation.append(("You", user_input))
            st.session_state.conversation.append(("Yago Assistant", response))

    for speaker, message in st.session_state.conversation:
        st.write(f"**{speaker}**: {message}")

if __name__ == "__main__":
    api_key = "enter your api key"
    configure_api(api_key)
    chatbot()
