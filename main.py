import streamlit as st
import json
from pathlib import Path
from models import LLM_DETAILS
from convesation_history import chdf

PERSONA_DATA = Path(__file__).parent / "data/persona.json"

persona = json.loads(PERSONA_DATA.read_text())
persona = {p["username"]: p["legacy_deva_id"] or p["id"] for p in persona}

# Username and deva id
username = st.selectbox(
    "Deva username",
    persona.keys()
)
deva_id = persona[username]

# Temperature
DEFAULT_TEMPERATURE = 0.2
temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, step=0.01, value=DEFAULT_TEMPERATURE)

# Model
model = st.selectbox("Model", LLM_DETAILS.keys(), format_func=lambda x: x.value)

# Max tokens
max_tokens = st.slider(
    "Max tokens",
    min_value=1,
    max_value=LLM_DETAILS[model].max_tokens,
    step=1,
    value=LLM_DETAILS[model].default_max_tokens,
)

st.text_area("Query")

st.write("Conversation history")
conversation_history = st.data_editor(
    chdf,
    num_rows="dynamic",
    use_container_width=True,
)
