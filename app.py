import streamlit as st

st.title("AI Image Generator & Editor")
st.write("Добре дошли! Тук можете да генерирате и редактирате изображения.")

prompt = st.text_input("Опишете какво искате да създадете:")
uploaded_file = st.file_uploader("Или качете снимка за редакция", type=["jpg", "png", "jpeg"])

if st.button("Генерирай / Обработи"):
    st.success(f"Готово! Обработен промпт: {prompt}")
