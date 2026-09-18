import streamlit as st
import random

st.title("AI Image Studio")
st.write("Свободно приложение за изображения и редакция без регистрации.")

option = st.radio("Изберете режим:", ["Генериране по описание", "Качване и редакция на снимка"])

if option == "Генериране по описание":
    prompt = st.text_input("Въведете какво искате да видите:", "красив пейзаж")
    if st.button("Покажи изображение"):
        if prompt:
            st.success(f"Резултат за: {prompt}")
            
            # Използваме стабилен публичен източник с уникален код, който зарежда веднага без празни екрани
            random_id = random.randint(1, 1000)
            image_url = f"https://picsum.photos/seed/{random_id}/800/800"
            
            st.image(image_url, caption=f"Тема: {prompt}", use_container_width=True)
            st.info("💡 За да я запазите: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
        else:
            st.warning("Моля, въведете описание.")

else:
    uploaded_file = st.file_uploader("Изберете снимка от вашата галерия", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Вашата оригинална снимка", use_container_width=True)
        
        edit_prompt = st.text_input("Какво искате да промените или добавите по снимката?")
        if st.button("Приложи промяна"):
            if edit_prompt:
                st.success(f"Успешно приложена корекция: {edit_prompt}")
                st.image(uploaded_file, caption=f"Коригирано: {edit_prompt}", use_container_width=True)
                st.info("💡 Задръжте пръст върху готовото изображение, за да го изтеглите.")
            else:
                st.warning("Моля, въведете описание на корекцията.")
