import streamlit as st
import urllib.parse

st.title("AI Image Studio")
st.write("Истински AI генератор по ваш текст без ограничения.")

prompt = st.text_input("Въведете описание на това, което искате да се генерира:", "кюфтета в чиния")

if st.button("Генерирай изображение"):
    if prompt:
        st.success(f"Генериране по текст: {prompt}")
        
        # Преобразуваме точно твоето описание в линк за генератора
        encoded = urllib.parse.quote(prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded}"
        
        # Показваме генерираното изображение директно
        st.markdown(f'<img src="{image_url}" style="width:100%; border-radius:10px;" alt="{prompt}">', unsafe_allow_html=True)
        st.info("💡 За да запазите изображението: Задръжте пръст върху него и изберете 'Изтегляне на изображение'.")
    else:
        st.warning("Моля, въведете описание.")
