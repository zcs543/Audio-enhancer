import streamlit as st
import noisereduce as nr
import librosa
import soundfile as sf
import io
import numpy as np

st.title("Vocal Enhancer & 400% Booster")
st.write("Upload audio to remove hiss and boost volume by 4x.")

uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"])

if uploaded_file:
    # 1. Load the audio
    st.info("Loading audio...")
    data, rate = librosa.load(uploaded_file, sr=None)
    
    # 2. Perform noise reduction
    st.info("Cleaning up background noise...")
    reduced_noise = nr.reduce_noise(y=data, sr=rate, prop_decrease=0.8)
    
    # 3. Boost Volume by 400% (4x)
    st.info("Boosting volume by 400%...")
    boosted_audio = reduced_noise * 4.0
    
    # 4. Prevent Clipping (Normalization)
    # This keeps the audio at the maximum safe volume if 4x is too loud
    max_val = np.max(np.abs(boosted_audio))
    if max_val > 1.0:
        boosted_audio = boosted_audio / max_val
    
    # 5. Save and Play
    buffer = io.BytesIO()
    sf.write(buffer, boosted_audio, rate, format='WAV')
    buffer.seek(0)
    
    st.success("Processing Complete!")
    st.audio(buffer, format='audio/wav')
    
    st.download_button(
        label="Download Boosted Audio",
        data=buffer,
        file_name="boosted_vocal.wav",
        mime="audio/wav"
    )
