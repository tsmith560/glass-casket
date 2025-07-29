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
    st.set_page_config(page_title="Glass Casket", layout="wide")
    st.title("🪞 Glass Casket")
    st.markdown("_A forensic interface to entombed oracles and faded thoughts._")

    choice = st.sidebar.selectbox("Choose a ritual:", [
        "🧠 Ask the Oracle",
        "🕸️ View Temporal Threads",
        "🪦 Model Necropolis"
    ])

    if choice == "🧠 Ask the Oracle":
        oracle = Oracle()
        question = st.text_input("Ask the Oracle:")
        if question:
            response = oracle.ask(question)
            st.markdown(f"🔮 **Oracle says:** {response}")

    elif choice == "🕸️ View Temporal Threads":
        st.markdown("### 🕸️ Thread Log")
        view_thread_log()

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
