import streamlit as st
import tempfile, os
from modules.loader_text import load_text_file
from modules.loader_audio import transcribe_audio
from modules.loader_video import transcribe_video_audio
from modules.loader_image import extract_image_text
from utils_chat import init_chat, ask

st.set_page_config(page_title="AZE LLM Cloud (OpenRouter)", layout="centered")
st.title("🤖 AZE LLM Cloud – Drop tes fichiers, discute avec ton IA (OpenRouter)")

if "history" not in st.session_state:
    st.session_state.history = init_chat()

uploaded = st.file_uploader("📁 Dépose ton fichier ici :", type=[
    "txt", "md", "pdf", "docx", "mp3", "wav", "mp4", "mov", "png", "jpg", "jpeg"
])

if uploaded:
    ext = uploaded.name.split('.')[-1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix='.'+ext) as tmp:
        tmp.write(uploaded.read())
        path = tmp.name

    if ext in ["txt", "md", "pdf", "docx"]:
        content = load_text_file(path)
    elif ext in ["mp3", "wav"]:
        content = transcribe_audio(path)
    elif ext in ["mp4", "mov", "mkv"]:
        content = transcribe_video_audio(path)
    else:
        content = extract_image_text(path)

    st.success("✅ Contenu extrait.")
    st.text_area("🧾 Aperçu :", content, height=200)
    st.session_state.history.append({"role": "system", "content": content})

prompt = st.text_input("💬 Pose ta question à l’IA")
if prompt:
    reply = ask(prompt, st.session_state.history)
    st.markdown(f"**Tu :** {prompt}")
    st.markdown(f"**AZE :** {reply}")
