import streamlit as st
import requests

# URL of the FastAPI backend
API_URL = "http://127.0.0.1:8001/chat/"

# Streamlit UI for chat
st.title("RAG Database Assistant")

# Initialize chat history in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# User prompt input
prompt = st.chat_input("Ask your queries!")

# If user submits a prompt, send it to FastAPI and store both user input and response
if prompt:
    # Add the user message to the session state
    st.session_state.messages.append({"user": "User", "message": prompt})
    
    # Send the message to the FastAPI backend
    response = requests.post(API_URL, json={"user": "User", "message": prompt})
    
    if response.status_code == 200:
        data = response.json()
        # Append Assistant response to the session state
        st.session_state.messages.append({"user": "Assistant", "message": data["response"]})
    else:
        st.session_state.messages.append({"user": "Assistant", "message": "Error: Could not connect to the backend."})

# Display chat history from session state
for message in st.session_state.messages:
    with st.chat_message(message["user"]):
        st.write(message["message"])
