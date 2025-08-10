# streamlit_app.py
from openai import OpenAI
import streamlit as st
from datetime import datetime

# ---------- Configuración de página ----------
st.set_page_config(
    page_title="Coach IA para Pilotos",
    page_icon="🛫",
    layout="wide",
    menu_items={"Get help": None, "Report a bug": None, "About": None},
)

# ---------- Estilos (CSS) ----------
st.markdown("""
<style>
/* ancho máximo y tipografía */
.main { max-width: 1200px; margin: 0 auto; }
.block-container { padding-top: 2rem; }
h1, h2, h3 { letter-spacing: .2px }

/* burbujas */
.chat-bubble { border-radius: 14px; padding: 12px 14px; line-height: 1.5 }
.user { background: #EDF2FF; border: 1px solid #D0D7FF }
.assistant { background: #F8F9FA; border: 1px solid #E9ECEF }

/* caja input pegada abajo */
.stChatInputContainer { position: sticky; bottom: 0; background: white; padding-top: 8px; }

/* footer sutil */
.footer { color:#6b7280; font-size:12px; text-align:center; margin-top:24px; }
</style>
""", unsafe_allow_html=True)

# ---------- Cliente OpenAI ----------
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
MODEL_ID = st.secrets.get("OPENAI_MODEL", "gpt-4o-mini")

client = OpenAI(api_key=OPENAI_API_KEY)

# ---------- Barra lateral ----------
st.sidebar.header("⚙️ Configuración")
temperature = st.sidebar.slider("Creatividad (temperature)", 0.0, 1.0, 0.3, 0.1)
st.sidebar.caption(f"Modelo: `{MODEL_ID}`")
if st.sidebar.button("🗑️ Limpiar chat"):
    st.session_state.messages = []
    st.rerun()

with st.sidebar.expander("Acerca de", expanded=False):
    st.write(
        "Chat de entrenamiento para pilotos (CBTA/EBT). "
        "Usa tu modelo fine‑tuned de OpenAI y guarda el historial en la sesión."
    )

# ---------- Estado de conversación ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Eres un coach de entrenamiento CBTA/EBT. Responde con precisión y claridad."}
    ]

# ---------- Cabecera ----------
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://em-content.zobj.net/thumbs/240/apple/354/airplane_2708-fe0f.png", width=60)
with col2:
    st.title("Coach IA para Pilotos")
    st.caption("Chat conectado a tu modelo fine‑tuned de OpenAI.")

# ---------- Mostrar historial ----------
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    avatar = "🧑‍✈️" if msg["role"] == "user" else "🤖"
    klass = "user" if msg["role"] == "user" else "assistant"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(f"<div class='chat-bubble {klass}'>{msg['content']}</div>", unsafe_allow_html=True)

# ---------- Entrada del usuario ----------
prompt = st.chat_input("Escribe tu consulta…")
if prompt:
    # pinta el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍✈️"):
        st.markdown(f"<div class='chat-bubble user'>{prompt}</div>", unsafe_allow_html=True)

    # llamada al modelo
    try:
        with st.chat_message("assistant", avatar="🤖"):
            thinking = st.status("Consultando al modelo…", expanded=False)
            resp = client.chat.completions.create(
                model=MODEL_ID,
                temperature=temperature,
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages if m["role"] != "system"]  # enviamos solo user/assistant
            )
            thinking.update(label="Respuesta recibida", state="complete")
            answer = resp.choices[0].message.content.strip()
            st.markdown(f"<div class='chat-bubble assistant'>{answer}</div>", unsafe_allow_html=True)
        # guardamos
        st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error("No pude obtener respuesta del modelo. Revisa tu API Key/Modelo o vuelve a intentar.")
        st.caption(f"Detalle técnico: {e}")

# ---------- Footer ----------
st.markdown(
    f"<div class='footer'>© {datetime.now().year} Coach IA — MVP1. "
    f"Esta demo usa OpenAI y Streamlit Cloud.</div>", unsafe_allow_html=True
)
