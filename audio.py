import streamlit as st
from df.enhance import enhance, init_df, load_audio, save_audio

# Load the AI model
model, df_state, _ = init_df()

st.title("Vocal Enhancer")
uploaded_file = st.file_uploader("Upload Audio (WAV/MP3)", type=["wav", "mp3"])

if uploaded_file:
    # Save uploaded file temporarily
    with open("input.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.info("Removing hiss and hum...")
    
    # Process audio
    audio, _ = load_audio("input.wav", sr=df_state.sr())
    enhanced = enhance(model, df_state, audio)
    
    # Save and display result
    save_audio("enhanced.wav", enhanced, df_state.sr())
    st.audio("enhanced.wav")
    st.success("Done!")