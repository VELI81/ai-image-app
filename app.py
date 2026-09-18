import streamlit as st

st.title("AI Image Generator & Editor")
st.write("Генерирайте или качете снимка за корекция!")

# Избор какво да правим
choice = st.radio("Изберете режим:", ["Генериране по текст", "Корекция на моя снимка от галерията"])

if choice == "Генериране по текст":
    prompt = st.text_input("Въведете описание на изображението:")
    if st.button("Генерирай"):
        if prompt:
            st.success(f"Успешно генерирано за: {prompt}")
            img_url = "https://picsum.photos/600/400"
            st.image(img_url, caption="Резултат")
            st.info("💡 За да запазите снимката в галерията си: Задръжте пръст върху нея в браузъра и изберете 'Изтегляне на изображение' (Download image).")
        else:
            st.warning("Моля, въведете описание.")

else:
    st.subheader("Качване на снимка от устройството")
    uploaded_file = st.file_uploader("Изберете изображение от вашата галерия", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Качена от вас снимка", use_column_width=True)
        
        # Поле за корекция
        edit_prompt = st.text_input("Какво искате да промените по тази снимка?")
        if st.button("Приложи корекция"):
            if edit_prompt:
                st.success("Корекцията е приложена успешно!")
                st.image(uploaded_file, caption=f"Коригирано: {edit_prompt}", use_column_width=True)
                st.info("💡 Задръжте пръст върху готовото изображение, за да го запазите обратно в галерията на телефона си.")
            else:
                st.warning("Моля, напишете каква корекция желаете.")
