import streamlit as st
from openai import OpenAI

st.markdown("<h2 style='text-align: center;'>Official AI Image Generator</h2>", unsafe_allow_html=True)
st.write("Студио за генерация на изображения с вашия личен API ключ.")

# Поле за въвеждане на ключа (парола, за да е скрит)
api_key = st.text_input("Въведете вашия OpenAI API ключ (sk-...):", type="password")

prompt = st.text_input("Въведете подробно описание на изображението:", "красив фотореалистичен пейзаж")

if st.button("Генерирай с AI"):
    if not api_key:
        st.warning("Моля, въведете вашия OpenAI API ключ в полето отгоре.")
    elif not prompt:
        st.warning("Моля, въведете описание.")
    else:
        try:
            # Инициализираме официалния клиент на OpenAI с твоя ключ
            client = OpenAI(api_key=api_key)
            
            with st.spinner("Изкуственият интелект генерира перфектната картина..."):
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )
                
                image_url = response.data[0].url
                
                st.success("Изображението е генерирано успешно!")
                st.image(image_url, caption=prompt, use_container_width=True)
                st.info("💡 За да я запазите в телефона си: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
                
        except Exception as e:
            st.error(f"Възникна грешка при генерацията: {e}")

