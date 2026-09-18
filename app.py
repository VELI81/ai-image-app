import streamlit as st

st.title("AI Image Generator")
st.write("Приложението работи успешно и е готово!")

prompt = st.text_input("Въведете описание на изображението:")

if st.button("Генерирай изображение"):
    if not prompt:
        st.warning("Моля, въведете описание!")
    else:
        st.success(f"Успешно генерирано изображение за: {prompt}")
        # Показваме примерна картинка за тест
        st.image("https://picsum.photos/600/400", caption=f"Резултат за: {prompt}")
