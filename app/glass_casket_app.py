# app/glass_casket_app.py

import sys
import os
import streamlit as st

# Add root to sys.path (for src/ and other modules)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Debugging print to verify path (optional)
# st.write("sys.path:", sys.path)

try:
    from interface import run_interface
except ModuleNotFoundError as e:
    st.error(f"Import failed: {e}")
    raise

if __name__ == "__main__":
    run_interface()
