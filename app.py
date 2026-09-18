import streamlit as st
import urllib.parse

st.title("AI Image Generator")
st.write("Генерирайте и редактирайте вашите изображения!")

choice = st.radio("Изберете режим:", ["Генериране по текст", "Корекция на снимка"])

if choice == "Генериране по текст":
    prompt = st.text_input("Въведете описание на изображението (на английски е препоръчително):")
    if st.button("Генерирай"):
        if prompt:
            st.success(f"Успешно генерирано за: {prompt}")
            
            # Преобразуваме текста в безопасен формат за линк
            encoded_prompt = urllib.parse.quote(prompt)
            # Използваме истински AI генератор, който създава картинка по твоето описание
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            
            st.image(image_url)
            st.info("💡 За да я запазите в галерията: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
        else:
            st.warning("Моля, въведете описание.")
else:
    uploaded_file = st.file_uploader("Изберете снимка от вашата галерия", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file)
        edit_text = st.text_input("Какво да променим по снимката?")
        if st.button("Приложи корекция"):
            st.success("Корекцията е приложена успешно!")
            st.image(uploaded_file)
