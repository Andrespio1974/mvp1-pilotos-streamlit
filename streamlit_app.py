import os
import streamlit as st
import requests

st.set_page_config(page_title="MVP1 · Coach IA para Pilotos", page_icon="🛫", layout="centered")

# --- Config & secrets ---
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = st.secrets.get("OPENAI_MODEL") or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
API_URL = "https://api.openai.com/v1/chat/completions"

st.title("🛫 Coach IA para Pilotos")
st.caption("Chat conectado a tu modelo fine‑tuned de OpenAI.")

if not OPENAI_API_KEY:
    st.warning("Configura `OPENAI_API_KEY` y `OPENAI_MODEL` en *Settings → Secrets* (Streamlit Cloud) o variables de entorno locales.")
    st.stop()

# --- Chat state ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render previous messages
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Input box
prompt = st.chat_input("Escribe tu consulta CBTA/EBT…")
if prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call OpenAI
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
    body = {
        "model": OPENAI_MODEL,
        "messages": st.session_state.messages,
        "temperature": 0.7,
    }
    try:
        r = requests.post(API_URL, headers=headers, json=body, timeout=60)
        r.raise_for_status()
        data = r.json()
        answer = data["choices"][0]["message"]["content"]
    except Exception as e:
        answer = f"❌ Error al llamar a OpenAI: {e}"

    # Render assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
