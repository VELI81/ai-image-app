import streamlit as st
import urllib.parse

st.markdown("<h2 style='text-align: center;'>True AI Generator</h2>", unsafe_allow_html=True)
st.write("Напълно свободен и точен AI генератор без ограничения.")

prompt = st.text_input("Въведете описание на изображението:", "cyberpunk city")

if st.button("Генерирай"):
    if prompt:
        with st.spinner("Генериране на изображение..."):
            # Кодираме промпта за сигурна връзка
            encoded_prompt = urllib.parse.quote(prompt)
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&noshuffle=true"
            
            st.success(f"Успешно генерирано за: {prompt}")
            
            # Използваме вградения st.image на Streamlit с официалния линк, което елиминира счупените иконки
            st.image(image_url, caption=prompt, use_container_width=True)
            st.info("💡 За да я запазите: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
    else:
        st.warning("Моля, въведете описание.")
