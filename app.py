import streamlit as st
import requests
from PIL import Image
import io

st.title("AI Image Generator")
st.write("Генерирайте уникални изображения с изкуствен интелект!")

prompt = st.text_input("Въведете описание на изображението на английски (напр. A futuristic city at sunset):")

if st.button("Генерирай изображение"):
    if not prompt:
        st.warning("Моля, въведете описание!")
    else:
        with st.spinner("Генерира се изображение, моля изчакайте..."):
            API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
            headers = {"Authorization": "Bearer hf_demo_key"}
            
            payload = {"inputs": prompt}
            response = requests.post(API_URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                image = Image.open(io.BytesIO(response.content))
                st.image(image, caption=f"Резултат за: {prompt}", use_column_width=True)
            else:
                st.error("Възникна грешка при свързването с AI модела. Опитайте отново по-късно.")

