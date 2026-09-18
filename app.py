import streamlit as st
import urllib.parse

st.title("AI Image Generator")
st.write("Генерирайте изображения директно по ваше описание!")

prompt = st.text_input("Въведете описание на изображението:", "animals in nature")

if st.button("Генерирай изображение"):
    if prompt:
        st.success(f"Генериране за: {prompt}")
        
        # Кодираме текста директно в линка, за да няма зависимост от външни преводачи
        encoded = urllib.parse.quote(prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded}"
        
        st.image(image_url, use_container_width=True)
        st.info("💡 За да я запазите: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
    else:
        st.warning("Моля, въведете описание.")
