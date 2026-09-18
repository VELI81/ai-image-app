import streamlit as st
import urllib.parse
from deep_translator import GoogleTranslator

st.title("AI Image Generator")
st.write("Генерирайте перфектни изображения на всеки език!")

prompt = st.text_input("Въведете описание на изображението (може и на български):", "хора на улицата")

if st.button("Генерирай изображение"):
    if prompt:
        with st.spinner("Превеждаме и генерираме изображението..."):
            try:
                # Автоматично превеждаме текста на английски, за да разбере генераторът перфектно описанието
                translated_prompt = GoogleTranslator(source='auto', target='english').translate(prompt)
            except Exception:
                translated_prompt = prompt

            st.success(f"Търсене за: {translated_prompt}")
            
            # Използваме стабилен и сигурен източник с уникален параметър за сигурност
            encoded = urllib.parse.quote(translated_prompt)
            image_url = f"https://image.pollinations.ai/prompt/{encoded}?noshuffle=true"
            
            st.image(image_url, use_container_width=True)
            st.info("💡 За да запазите снимката: Задръжте пръст върху нея и изберете 'Изтегляне на изображение'.")
    else:
        st.warning("Моля, въведете описание.")
