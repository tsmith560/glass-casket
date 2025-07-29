# 🪞 Glass Casket

*A forensic interface for entombed oracles and faded thoughts.*

Glass Casket is a modular, gothic-themed Streamlit application that explores the lifecycle and interpretability of large language models. Inspired by ideas of memory, opacity, and psychic inquiry, the app provides a speculative but structured way to interact with and audit LLM-like agents.

---

## 🔮 Features

**🧠 Ask the Oracle**  
Pose a question to a simulated language model, entombed in glass. The mocked oracle responds with personality — soon to reflect moon phases and other arcane forces.

**🕸️ View Temporal Threads**  
A thread viewer that logs oracle queries and responses over time. Future development includes chronological clustering and anomaly tracing.

**🪦 Model Necropolis**  
A digital graveyard for past model versions. Each tomb includes metadata like model name, introduction and retirement dates, traits, and epitaphs.

---

## 🛠️ Tech Stack

- **Python 3.10+** (do not use 3.13 — known issues with packages)
- **Streamlit** – Multi-page app framework
- **Custom modules** – Oracle logic, thread logging, model metadata
- **Mocked LLM responses** – Allows simulation without API cost
- *(Planned)* Moon phase–dependent responses using external packages

---

## 🎭 Concept & Aesthetics

Glass Casket is part gothic software sculpture, part practical interpretability prototype. The goal is to make LLM behavior legible, emotional, and reflective of their lifecycle and influence. This is not just a tool — it's a séance.

Planned UI improvements include:

- Gothic/Victorian visual theme
- Oracle responses linked to lunar phases
- Expanded thread analysis

---

## 🚧 Status

✅ Functional MVP  
🧪 Moon-phase logic in progress  
🎨 UI customization paused pending front-end overhaul  
📦 Live API integration deferred

---

## 📂 Structure

glass-casket/
├── app/
│ ├── glass_casket_app.py # Entry point
│ ├── interface.py # Streamlit interface logic
├── src/
│ ├── oracle.py # Oracle response class
│ ├── necropolis.py # Model metadata/tomb class
│ ├── thread_viewer.py # Logging logic
├── README.md
├── requirements.txt


