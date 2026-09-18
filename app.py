import streamlit as st
import urllib.parse

st.title("AI Image Generator")
st.write("Свободен генератор на изображения без ограничения.")

prompt = st.text_input("Въведете какво да бъде изобразено:", "future city")

if st.button("Генерирай"):
    if prompt:
        st.success(f"Генериране: {prompt}")
        
        # Директно кодиране на текста за максимална свобода и бързина
        encoded = urllib.parse.quote(prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded}"
        
        st.image(image_url, use_container_width=True)
        st.info("💡 За да я запазите: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
    else:
        st.warning("Моля, въведете описание.")
