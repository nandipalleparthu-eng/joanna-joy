import streamlit as st

st.set_page_config(page_title="🌸 For You, Joanna", layout="centered")

st.markdown("""
<style>
body { background-color: #0d0d14; }
.block-container { max-width: 480px; padding-top: 2rem; }
h1 { text-align: center; color: #f0c8d8; }
p  { text-align: center; color: #8a7a9a; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🌸 For You, Joanna</h1>", unsafe_allow_html=True)
st.markdown("<p>LILIUM ORIENTALIS · 3D PARAMETRIC BOTANICAL ANIMATION</p>", unsafe_allow_html=True)
st.markdown("---")

with open("lily_3d_botanical_animation.mp4", "rb") as f:
    video_bytes = f.read()

st.video(video_bytes)
