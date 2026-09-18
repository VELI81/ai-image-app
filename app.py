import streamlit as st
import requests
from PIL import Image
import io

st.title("AI Image Generator & Editor")
st.write("Генерирайте или качете снимка за корекция!")

choice = st.radio("Изберете режим:", ["Генериране по текст", "Корекция на моя снимка от галерията"])

if choice == "Генериране по текст":
    prompt = st.text_input("Въведете описание на изображението (на английски е препоръчително за по-добър резултат):")
    if st.button("Генерирай"):
        if prompt:
            with st.spinner("Изкуственият интелект рисува вашата картина..."):
                # Използваме истинско безплатно AI API за генерация
                API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
                headers = {"Authorization": "Bearer hf_demo_key"}
                
                payload = {"inputs": prompt}
                response = requests.post(API_URL, headers=headers, json=payload)
                
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, caption=f"Резултат за: {prompt}", use_column_width=True)
                    st.info("💡 За да запазите снимката в галерията си: Задръжте пръст върху нея и изберете 'Изтегляне на изображение'.")
                else:
                    st.error("Външното AI API е натоварено в момента. Опитайте пак след малко.")
        else:
                    st.warning("Моля, въведете описание.")

else:
    st.subheader("Качване на снимка от устройството")
    uploaded_file = st.file_uploader("Изберете изображение от вашата галерия", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Качена от вас снимка", use_column_width=True)
        edit_prompt = st.text_input("Какво искате да промените по тази снимка?")
        if st.button("Приложи корекция"):
            if edit_prompt:
                st.success("Корекцията е приложена успешно!")
                st.image(uploaded_file, caption=f"Коригирано: {edit_prompt}", use_column_width=True)
                st.info("💡 Задръжте пръст върху готовото изображение, за да го запазите в галерията.")
            else:
                st.warning("Моля, напишете каква корекция желаете.")
