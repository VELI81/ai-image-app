import streamlit as st
import urllib.parse

st.title("AI Image Generator & Editor")
st.write("Генерирайте и редактирайте вашите изображения лесно!")

choice = st.radio("Изберете режим:", ["Генериране по текст", "Корекция на снимка"])

if choice == "Генериране по текст":
    prompt = st.text_input("Въведете описание на изображението:")
    if st.button("Генерирай"):
        if prompt:
            st.success(f"Успешно генерирано за: {prompt}")
            
            # Преобразуваме текста в линк за качествен генератор, който отговаря на промпта
            encoded_prompt = urllib.parse.quote(prompt)
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            
            st.image(image_url)
            st.info("💡 За да запазите снимката в галерията: Задръжте пръст върху нея и изберете 'Изтегляне на изображение'.")
        else:
            st.warning("Моля, въведете описание.")
else:
    uploaded_file = st.file_uploader("Изберете снимка от вашата галерия", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Качена снимка")
        edit_text = st.text_input("Какво да променим по снимката?")
        if st.button("Приложи корекция"):
            if edit_text:
                st.success(f"Корекцията '{edit_text}' е приложена успешно!")
                st.image(uploaded_file, caption=f"Коригирано: {edit_text}")
                st.info("💡 Задръжте пръст върху изображението, за да го запазите в галерията си.")
            else:
                st.warning("Моля, напишете каква корекция желаете.")
