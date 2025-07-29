# main.py
import streamlit as st
from src.oracle import Oracle
from src.thread_viewer import view_thread_log  # We'll make this in a sec

st.set_page_config(page_title="Glass Casket", layout="wide")
st.title("🪞 Glass Casket: Black Box Interface")

tabs = st.tabs(["🔮 Ask the Oracle", "🧠 Synapse Trace", "🏛️ Necropolis (Soon)"])

# 1. Ask the Oracle
with tabs[0]:
    st.header("🔮 Ask the Oracle")
    question = st.text_input("Pose your question to the Oracle:")
    if st.button("Submit"):
        if question.strip():
            oracle = Oracle()
            response = oracle.ask_oracle(question)
            st.markdown(f"**Oracle Responds:**\n> {response}")
        else:
            st.warning("You must enter a question.")

# 2. Synapse Trace
with tabs[1]:
    st.header("🧠 Synapse Trace")
    view_thread_log()

# 3. Necropolis placeholder
with tabs[2]:
    st.header("🏛️ Necropolis")
    st.info("The library of echoes has not yet been opened.")

# View thread log
with st.expander("📜 Thread History"):
    st.text(view_thread_log())

