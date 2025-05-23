from backend import *
import streamlit as st
import requests
import json
import time

def response_generator(question):
    response = requests.post("http://172.16.11.6:5001/query", 
                json={
                    "question": question
                })
    botresponse = json.loads(response.text)
    for word in botresponse["response"].split():
        yield word + " "
        time.sleep(0.05)

st.title("The Analyst")

csv_data = st.text_input("",placeholder="upload the csv path")
if csv_data:
    response = requests.post("http://172.16.11.6:5001/upload", 
                json={
                    "file_path": csv_data
                })
    res = json.loads(response.text)
    st.success(res['message'])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})