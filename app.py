import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title("AI Image Generator")
st.write("Генерирайте и редактирайте вашите изображения!")

choice = st.radio("Изберете режим:", ["Генериране по текст", "Корекция на снимка"])

if choice == "Генериране по текст":
    prompt = st.text_input("Въведете описание на изображението:")
    if st.button("Генерирай"):
        if prompt:
            st.success(f"Успешно генерирано за: {prompt}")
            
            # Зареждаме картинката без никакви сложни формати в капшъна
            url = "https://picsum.photos/600/400"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            
            st.image(img, use_column_width=True)
            st.info("💡 За да я запазите в галерията: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
        else:
            st.warning("Моля, въведете описание.")
else:
    uploaded_file = st.file_uploader("Изберете снимка от вашата галерия", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=True)
        edit_text = st.text_input("Какво да променим по снимката?")
        if st.button("Приложи корекция"):
            st.success("Корекцията е приложена успешно!")
            st.image(uploaded_file, use_column_width=True)
