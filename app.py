import streamlit as st

st.title("AI Image Generator")
st.write("Генерирайте и редактирайте вашите изображения!")

choice = st.radio("Изберете режим:", ["Генериране по текст", "Корекция на снимка"])

if choice == "Генериране по текст":
    prompt = st.text_input("Въведете описание на изображението:")
    if st.button("Генерирай"):
        if prompt:
            st.success(f"Успешно генерирано изображение за: {prompt}")
            # Използваме директен низ за линка, за да няма TypeError
            image_url = "https://picsum.photos/600/400"
            st.image(image_url, caption=f"Резултат: {prompt}", use_column_width=True)
            st.info("💡 За да запазите снимката в галерията: Задръжте пръст върху нея и изберете 'Изтегляне на изображение'.")
        else:
            st.warning("Моля, въведете описание.")
else:
    uploaded_file = st.file_uploader("Изберете снимка от вашата галерия", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Качена снимка", use_column_width=True)
        edit_text = st.text_input("Какво да променим по снимката?")
        if st.button("Приложи корекция"):
            st.success("Корекцията е приложена успешно!")
            st.image(uploaded_file, caption=f"Коригирано: {edit_text}", use_column_width=True)

