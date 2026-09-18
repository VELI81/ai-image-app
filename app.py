import streamlit as st
import urllib.parse

st.markdown("<h2 style='text-align: center;'>Unrestricted AI Studio</h2>", unsafe_allow_html=True)
st.write("Напълно свободен генератор без ограничения и цензура.")

prompt = st.text_input("Въведете какво да се генерира:", "futuristic cyberpunk city")

if st.button("Генерирай без ограничения"):
    if prompt:
        st.success(f"Генериране за: {prompt}")
        
        # Кодираме текста директно за безцензурен изход
        encoded_prompt = urllib.parse.quote(prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?seed=42&noshuffle=true"
        
        # Използваме директен iframe за стопроцентово сигурно показване без счупени иконки
        st.markdown(f'''
            <div style="width: 100%; text-align: center;">
                <img src="{image_url}" style="width: 100%; border-radius: 10px;" />
            </div>
        ''', unsafe_allow_html=True)
        
        st.info("💡 За да я запазите: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
    else:
        st.warning("Моля, въведете описание.")
