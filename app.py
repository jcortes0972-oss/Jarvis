import os
import streamlit as st
from streamlit_mic_recorder import speech_to_text
from openai import OpenAI
from gtts import gTTS

st.set_page_config(page_title="JARVIS Terminal", page_icon="🤖", layout="centered")

# Custom Neon Hologram Styling
st.markdown("""
    <style>
    .stApp { background-color: #0a0f1d; color: #00f3ff; }
    h1 { color: #00f3ff; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00f3ff; }
    </style>
""", unsafe_allow_html=True)

st.title("J.A.R.V.I.S. Core Interface")
st.write("Status: ONLINE | Systems: HANDS-FREE VOICE READY")

# Initialize AI Brain
client = OpenAI(
    base_url="https://azure.com",
    api_key=os.environ.get("GITHUB_TOKEN")
)

# Automated Speech to Text component
# This opens your browser's native mic and automatically transcribes when you speak
text_input = speech_to_text(
    start_prompt="🎙️ Click once to activate continuous listening",
    stop_prompt="🛑 Stop listening",
    language='en',
    use_container_width=True,
    key='jarvis_mic'
)

if text_input:
    st.markdown(f"**You:** {text_input}")
    
    # Process with Llama 3
    with st.spinner("🤖 JARVIS is processing..."):
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are JARVIS, a highly sophisticated, witty, and loyal AI assistant. Address the user as Sir."},
                {"role": "user", "content": text_input}
            ],
            model="meta-llama-3-70b-instruct"
        )
        reply = response.choices.message.content
    
    st.markdown(f"**JARVIS:** {reply}")
    
    # Generate Voice and play it automatically via browser audio player
    tts = gTTS(text=reply, lang='en', tld='co.uk')
    tts.save("web_response.mp3")
    st.audio("web_response.mp3", format="audio/mp3", autoplay=True)
