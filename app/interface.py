# interface.py

import streamlit as st
from oracle import Oracle
from thread_viewer import view_thread

# Instantiate the Oracle
oracle = Oracle()

st.set_page_config(page_title="🕯️ Glass Casket", layout="centered")

st.title("🕯️ The Glass Casket")
st.markdown("**Speak your question into the void.** The Oracle will respond...")

# Input field for user question
question = st.text_input("🗣️ What do you ask the Oracle?", "")

# Button to submit question
if st.button("Summon Oracle"):
    if question.strip():
        response = oracle.ask_oracle(question)
        st.markdown("🔮 **The Oracle replies:**")
        st.markdown(f"> {response}")
    else:
        st.warning("Ask a real question, mortal.")

# Divider
st.markdown("---")

# Thread viewer section
st.markdown("### 🧵 Thread History")
st.text("Below are your past communions with the Oracle:")

# View the log file history
try:
    with open("thread_log.json", "r") as f:
        import json
        log = json.load(f)
        for entry in reversed(log):
            st.markdown(f"**🕰️ {entry['timestamp']}**")
            st.markdown(f"**⚰️ You:** {entry['question']}")
            st.markdown(f"**🔮 Oracle:** {entry['response']}")
            st.markdown("---")
except FileNotFoundError:
    st.info("No previous interactions found.")


# The Necropolis
st.markdown("---")
st.header("🏛️ Necropolis")
st.markdown("_A cryptic archive of every whisper and answer heard in the casket._")

entries = get_all_log_entries()

if entries:
    for entry in reversed(entries):  # newest first
        with st.container():
            st.markdown(f"**🕰️ {entry['timestamp']}**")
            st.markdown(f"**⚰️ You:** {entry['question']}")
            st.markdown(f"**🔮 Oracle:** {entry['response']}")
            st.markdown("---")
else:
    st.info("The Necropolis is empty. No tombs have been erected yet.")