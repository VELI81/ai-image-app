import streamlit as st
import urllib.parse

st.title("AI Image Generator")
st.write("Генерирайте изображения точно по ваш промпт!")

prompt = st.text_input("Въведете описание (на английски е най-добре, напр. 'people on the street'):", "people on the street")

if st.button("Генерирай"):
    if prompt:
        st.success(f"Успешно генерирано за: {prompt}")
        encoded = urllib.parse.quote(prompt)
        # Използваме директен и бърз AI генератор
        url = f"https://image.pollinations.ai/prompt/{encoded}"
        st.image(url)
        st.info("💡 За да я запазите: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
    else:
        st.warning("Моля, въведете описание.")
