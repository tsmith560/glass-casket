import streamlit as st
from oracle import Oracle
from thread_viewer import view_thread
import json

# Title
st.title("🪞 The Glass Casket")
st.markdown("An interface for exhuming machine memory.")

# Initialize Oracle
oracle = Oracle()

# Input
question = st.text_input("Ask the Oracle:", "")

if st.button("🕯️ Summon"):
    if question:
        response = oracle.ask_oracle(question)
        st.markdown(f"**⚰️ You:** {question}")
        st.markdown(f"**🔮 Oracle:** {response}")
    else:
        st.warning("You must enter a question to summon the Oracle.")

# Expandable thread viewer
with st.expander("📜 View Past Threads"):
    try:
        with open("thread_log.json", "r") as f:
            log = json.load(f)
            for entry in reversed(log):
                st.markdown(f"**🕰️ {entry['timestamp']}**")
                st.markdown(f"⚰️ *You:* {entry['question']}")
                st.markdown(f"🔮 *Oracle:* {entry['response']}")
                st.markdown("---")
    except FileNotFoundError:
        st.info("No past threads found.")
