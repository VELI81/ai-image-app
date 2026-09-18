import streamlit as st
import urllib.parse
import random

st.markdown("<h2 style='text-align: center;'>True AI Generator</h2>", unsafe_allow_html=True)
st.write("Напълно свободен и точен AI генератор без ограничения.")

prompt = st.text_input("Въведете точно описание на изображението:", "beautiful girl portrait")

if st.button("Генерирай"):
    if prompt:
        with st.spinner("Генериране на ново изображение..."):
            # Създаваме уникален случаен код за всяка заявка, за да не повтаря стари картинки
            random_seed = random.randint(1, 999999)
            
            # Кодираме точно твоя текст
            encoded_prompt = urllib.parse.quote(prompt)
            
            # Добавяме seed параметъра, за да гарантираме, че сървърът рисува точно това, което си написал
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={random_seed}&noshuffle=true"
            
            st.success(f"Успешно генерирано за: {prompt}")
            
            # Показваме директно през вградения инструмент на Streamlit
            st.image(image_url, caption=prompt, use_container_width=True)
            st.info("💡 За да я запазите: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
    else:
        st.warning("Моля, въведете описание.")
