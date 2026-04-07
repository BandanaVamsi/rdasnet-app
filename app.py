import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

st.set_page_config(layout="wide")
st.title("🛰️ RDASNet Satellite Denoising")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('RDASNet_v2_latest.keras')

model = load_model()

uploaded = st.file_uploader("Upload noisy image", type=['png','jpg'])
if uploaded:
    img
