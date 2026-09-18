import streamlit as st
import urllib.parse

st.markdown("<h2 style='text-align: center;'>AI Real Image Studio</h2>", unsafe_allow_html=True)
st.write("Генерирайте и визуализирайте изображения директно тук.")

prompt = st.text_input("Въведете описание на изображението:", "кюфтета в чиния")

if st.button("Покажи изображението"):
    if prompt:
        st.success(f"Генериране за: {prompt}")
        
        # Създаваме перфектен линк с параметри за високо качество
        encoded = urllib.parse.quote(f"{prompt}, hyperrealistic photography, 8k, detailed")
        image_url = f"https://image.pollinations.ai/prompt/{encoded}?noshuffle=true"
        
        # Показваме картинката директно чрез сигурен HTML контейнер
        st.markdown(f'''
            <div style="display: flex; justify-content: center;">
                <img src="{image_url}" style="width: 100%; max-width: 600px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
            </div>
        ''', unsafe_allow_html=True)
        
        st.info("💡 За да я запазите в телефона си: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
    else:
        st.warning("Моля, въведете описание.")
