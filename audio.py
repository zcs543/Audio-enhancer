import streamlit as st
import torch
from df.enhance import enhance, init_df, load_audio, save_audio

# This initializes the AI model
model, df_state, _ = init_df()

st.title("Vocal Enhancer")
uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if uploaded_file:
    # Save the file temporarily
    with open("input.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.info("Processing... cleaning up background noise.")
    
    # Run the noise reduction
    audio, _ = load_audio("input.wav", sr=df_state.sr())
    enhanced = enhance(model, df_state, audio)
    
    # Save the clean version
    save_audio("enhanced.wav", enhanced, df_state.sr())
    
    st.audio("enhanced.wav")
    st.success("Cleaned audio is ready!")
