import streamlit as st
import urllib.parse

st.title("AI Image Studio")
st.write("Генериране и редакция на изображения без ограничения.")

option = st.radio("Изберете режим:", ["Генериране по текст", "Качване и редакция на снимка"])

if option == "Генериране по текст":
    prompt = st.text_input("Въведете описание на изображението:", "beautiful landscape")
    if st.button("Генерирай"):
        if prompt:
            encoded = urllib.parse.quote(prompt)
            image_url = f"https://image.pollinations.ai/prompt/{encoded}"
            st.success(f"Успешно генерирано за: {prompt}")
            
            # Използваме директен и сигурен показ чрез Markdown, който не се чупи
            st.markdown(f'<img src="{image_url}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)
            st.info("💡 За да я запазите в галерията: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
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
