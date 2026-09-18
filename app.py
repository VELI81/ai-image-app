import streamlit as st
import urllib.parse

st.title("AI Prompt & Idea Studio")
st.write("Генерирайте ултра-реалистични описания за перфектни изображения без цензура.")

user_input = st.text_input("Въведете какво искате да създадете (на български):", "кюфтета в чиния")

if st.button("Създай перфектен промпт"):
    if user_input:
        # Създаваме професионален фотореалистичен промпт
        pro_prompt = f"Hyperrealistic photo of {user_input}, 8k resolution, photorealistic, highly detailed, professional studio lighting, cinematic shot, sharp focus"
        
        st.success("Готово! Копирайте този перфектен текст и го поставете в който и да е свободен AI генератор:")
        st.code(pro_prompt, language="text")
        
        # Директен линк към търсене за улеснение
        encoded = urllib.parse.quote(pro_prompt)
        st.markdown(f"🔗 [Отворете директно в свободен генератор](https://image.pollinations.ai/prompt/{encoded})")
    else:
        st.warning("Моля, въведете текст.")
