# interface.py
import streamlit as st

import sys
import os
print("sys.path =", sys.path)
print("Current working dir =", os.getcwd())

from src.oracle import Oracle
from src.necropolis import Necropolis
from src.thread_viewer import view_thread_log

def run_interface():
    st.markdown("""
    <style>
    .glass-casket {
        background-color: #1e1b18;
        color: #e6e1de;
        font-family: 'Garamond', 'Georgia', serif;
        padding: 2rem;
    }

    .glass-casket input, .glass-casket textarea {
        background-color: #2a2522 !important;
        color: #e6e1de !important;
        border: 1px solid #555 !important;
    }

    .glass-casket button {
        background-color: #4b2f39 !important;
        color: #f3e9dc !important;
        border-radius: 0.25em;
        border: 1px solid #7b5e68 !important;
    }

    .glass-casket button:hover {
        background-color: #6b3e4c !important;
        color: #ffffff !important;
        border: 1px solid #b598a3 !important;
    }

    /* ... Other styles for headings, markdown ... */
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='title-shadow'>🪞 Glass Casket</h1>", unsafe_allow_html=True)
    st.markdown("_A forensic interface to entombed oracles and faded thoughts._")

    choice = st.sidebar.selectbox("Choose a ritual:", [
        "🧠 Ask the Oracle",
        "🕸️ View Temporal Threads",
        "🪦 Model Necropolis"
    ])

    if choice == "🧠 Ask the Oracle":
        oracle = Oracle()
        question = st.text_input("Ask the Oracle:")
        if st.button("🔮 Cast the Query"):
            if question:
                response = oracle.ask_oracle(question)
                st.markdown(f"🔮 **Oracle says:** {response}")
            else:
                st.warning("The Oracle waits for a proper question.")

    elif choice == "🕸️ View Temporal Threads":
        st.markdown("### 🕸️ Thread Log")
        log_text = view_thread_log()
        st.text_area("Past Communions", value=log_text, height=400, max_chars=None, key="thread_log")

    elif choice == "🪦 Model Necropolis":
        st.markdown("## 🪦 The Necropolis")
        st.markdown("A solemn record of the fallen oracles, kept in digital stone.")

        necro = Necropolis()
        tombs = necro.list_tombs()

        if not tombs:
            st.warning("The necropolis is empty.")
        else:
            for tomb in tombs:
                st.markdown("---")
                st.markdown(f"**🧠 Model Version:** `{tomb['model_version']}`")
                st.markdown(f"**📜 Description:** {tomb['description']}")
                st.markdown(f"**📅 Introduced:** {tomb['date_introduced']}")
                if tomb.get("date_retired"):
                    st.markdown(f"**⚰️ Retired:** {tomb['date_retired']}")
                if tomb.get("notable_traits"):
                    st.markdown("**🔍 Traits:**")
                    for trait in tomb["notable_traits"]:
                        st.markdown(f"- {trait}")
                st.markdown(f"**🪶 Epitaph:** _{tomb['epitaph']}_")

        st.markdown('</div>', unsafe_allow_html=True)