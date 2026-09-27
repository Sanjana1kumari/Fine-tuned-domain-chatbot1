import streamlit as st
import requests


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="E-Commerce AI Support",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Header
# -----------------------------

st.title("🤖 E-Commerce AI Support")

st.caption(
    "AI-powered customer support for orders, "
    "returns, refunds, delivery and payments."
)


# -----------------------------
# FastAPI URL
# -----------------------------

API_URL = "http://127.0.0.1:8000/chat"


# -----------------------------
# Conversation Memory
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display Previous Messages
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# -----------------------------
# User Input
# -----------------------------

user_message = st.chat_input(
    "Ask about your order, refund, return..."
)


if user_message:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):
        st.write(user_message)


    # -------------------------
    # Create conversation context
    # -------------------------

    conversation = ""

    for message in st.session_state.messages[-6:]:

        role = message["role"]

        if role == "user":
            conversation += (
                "Customer: "
                + message["content"]
                + "\n"
            )

        else:
            conversation += (
                "Assistant: "
                + message["content"]
                + "\n"
            )


    # -------------------------
    # Send request to FastAPI
    # -------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "message": conversation
                    },
                    timeout=120
                )


                if response.status_code == 200:

                    data = response.json()

                    bot_response = data["answer"]

                else:

                    bot_response = (
                        "Sorry, the chatbot API "
                        "returned an error."
                    )


            except requests.exceptions.RequestException:

                bot_response = (
                    "Unable to connect to the chatbot API. "
                    "Please make sure FastAPI is running."
                )


        st.write(bot_response)


    # Save assistant response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_response
        }
    )


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("💬 E-Commerce Assistant")

    st.write("I can help with:")

    st.write("📦 Order tracking")
    st.write("↩️ Returns")
    st.write("💰 Refunds")
    st.write("🚚 Delivery")
    st.write("💳 Payments")
    st.write("❌ Cancellation")
    st.write("📱 Product issues")
    st.write("👤 Account problems")


    st.divider()


    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()