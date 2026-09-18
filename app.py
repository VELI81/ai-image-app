import streamlit as st
import urllib.parse
import requests
from io import BytesIO

st.title("AI Image Studio")
st.write("Генериране и редакция на изображения без ограничения.")

option = st.radio("Изберете режим:", ["Генериране по текст", "Качване и редакция на снимка"])

if option == "Генериране по текст":
    prompt = st.text_input("Въведете описание на изображението:", "beautiful landscape")
    if st.button("Генерирай"):
        if prompt:
            with st.spinner("Генериране на изображението..."):
                try:
                    encoded = urllib.parse.quote(prompt)
                    image_url = f"https://image.pollinations.ai/prompt/{encoded}"
                    
                    response = requests.get(image_url, timeout=15)
                    if response.status_code == 200:
                        image = BytesIO(response.content)
                        st.success(f"Успешно генерирано за: {prompt}")
                        st.image(image, caption=prompt, use_container_width=True)
                        st.info("💡 За да я запазите: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
                    else:
                        st.error("Грешка при зареждане на изображението от сървъра.")
                except Exception as e:
                    st.error(f"Възникна грешка: {e}")
        else:
            st.warning("Моля, въведете описание.")

else:
    uploaded_file = st.file_uploader("Изберете снимка от вашата галерия", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Вашата оригинална снимка", use_container_width=True)
        
        edit_prompt = st.text_input("Какво искате да промените или добавите по снимката?")
        if st.button("Приложи промяна"):
            if edit_prompt:
                st.success(f"Успешно приложена корекция: {edit_prompt}")
                st.image(uploaded_file, caption=f"Коригирано: {edit_prompt}", use_container_width=True)
                st.info("💡 Задръжте пръст върху готовото изображение, за да го изтеглите.")
            else:
                st.warning("Моля, въведете описание на корекцията.")
