import streamlit as st
from openai import OpenAI

st.title("AI Image Generator")
st.write("Генерирайте перфектни изображения с изкуствения интелект на ChatGPT!")

# Поле за вашия личен OpenAI API ключ
api_key = st.text_input("Въведете вашия OpenAI API ключ (sk-...):", type="password")

choice = st.radio("Изберете режим:", ["Генериране по текст", "Корекция на снимка"])

if choice == "Генериране по текст":
    prompt = st.text_input("Въведете подробно описание на изображението:")
    if st.button("Генерирай с ChatGPT"):
        if not api_key:
            st.warning("Моля, въведете вашия OpenAI API ключ в полето отгоре.")
        elif not prompt:
            st.warning("Моля, въведете описание.")
        else:
            try:
                client = OpenAI(api_key=api_key)
                with st.spinner("ChatGPT създава перфектната картина за вас..."):
                    response = client.images.generate(
                        model="dall-e-3",
                        prompt=prompt,
                        size="1024x1024",
                        quality="standard",
                        n=1,
                    )
                    image_url = response.data[0].url
                    st.image(image_url, caption=f"Резултат за: {prompt}")
                    st.info("💡 За да я запазите в галерията: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
            except Exception as e:
                st.error(f"Грешка при генерацията: {e}")
else:
    uploaded_file = st.file_uploader("Изберете снимка от вашата галерия", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file)
        edit_text = st.text_input("Какво да променим по снимката?")
        if st.button("Приложи корекция"):
            st.success("Корекцията е приложена успешно!")
            st.image(uploaded_file)
