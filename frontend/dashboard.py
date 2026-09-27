import os
import pandas as pd
import streamlit as st


# ==========================================
# Page configuration
# ==========================================

st.set_page_config(
    page_title="Chatbot Analytics",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# Title
# ==========================================

st.title("📊 E-Commerce Chatbot Analytics")

st.write(
    "Monitor chatbot usage, categories and response performance."
)


# ==========================================
# Log file
# ==========================================

LOG_FILE = "./logs/chatbot_logs.csv"


if not os.path.exists(LOG_FILE):

    st.warning(
        "No chatbot logs found yet. "
        "Use the chatbot first to generate data."
    )

    st.stop()


# ==========================================
# Load logs
# ==========================================

df = pd.read_csv(LOG_FILE)


# ==========================================
# Handle empty logs
# ==========================================

if df.empty:

    st.warning("The log file is empty.")

    st.stop()


# ==========================================
# Convert response time
# ==========================================

df["response_time_seconds"] = pd.to_numeric(
    df["response_time_seconds"],
    errors="coerce"
)


# ==========================================
# KPI calculations
# ==========================================

total_queries = len(df)

average_response_time = (
    df["response_time_seconds"].mean()
)

categories = df["category"].nunique()


# ==========================================
# KPI display
# ==========================================

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Queries",
        total_queries
    )


with col2:

    st.metric(
        "Average Response Time",
        f"{average_response_time:.2f} sec"
    )


with col3:

    st.metric(
        "Categories",
        categories
    )


st.divider()


# ==========================================
# Category distribution
# ==========================================

st.subheader("📌 Query Categories")

category_counts = (
    df["category"]
    .value_counts()
)

st.bar_chart(category_counts)


# ==========================================
# Response time
# ==========================================

st.subheader("⚡ Response Time")

st.line_chart(
    df["response_time_seconds"]
)


# ==========================================
# Recent conversations
# ==========================================

st.subheader("💬 Recent Conversations")

display_columns = [
    "timestamp",
    "question",
    "answer",
    "category",
    "response_time_seconds"
]

st.dataframe(
    df[display_columns].tail(20),
    use_container_width=True
)