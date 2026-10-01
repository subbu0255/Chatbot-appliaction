import os

import requests
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

API_URL = "http://127.0.0.1:8000/chat"
API_KEY = os.getenv("CHATBOT_API_KEY")

if not API_KEY:
    st.error("CHATBOT_API_KEY is missing from .env")
    st.stop()


st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")
st.write(
    "Beginner AI Chatbot using "
    "Streamlit + FastAPI + Groq"
)


if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_message = st.chat_input("Ask me anything...")


if user_message:
    with st.chat_message("user"):
        st.write(user_message)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    data = {
        "message": user_message
    }

    if st.session_state.conversation_id:
        data["conversation_id"] = (
            st.session_state.conversation_id
        )

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.post(
            API_URL,
            json=data,
            headers=headers,
            timeout=60
        )

        if response.status_code == 200:
            result = response.json()

            answer = result["answer"]

            st.session_state.conversation_id = (
                result["conversation_id"]
            )

            with st.chat_message("assistant"):
                st.write(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        elif response.status_code == 401:
            st.error("Authentication failed.")

        else:
            st.error(
                f"API Error: {response.status_code} - "
                f"{response.text}"
            )

    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to the chatbot API. "
            "Make sure FastAPI is running."
        )

    except requests.exceptions.Timeout:
        st.error("The AI service took too long to respond.")
