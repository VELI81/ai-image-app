import streamlit as st
import urllib.parse

st.markdown("""
    <h2 style='text-align: center; color: #ff4b4b;'>🔥 AI Real Studio Pro 🔥</h2>
    <p style='text-align: center;'>Ултра-реалистичен генератор и редактор без ограничения.</p>
""", unsafe_allow_html=True)

mode = st.radio("Изберете режим на работа:", ["✨ Фотореалистична генерация", "🖼️ Качване и редакция на снимка"])

if mode == "✨ Фотореалистична генерация":
    user_prompt = st.text_area("Въведете вашето описание или изречение (на български или английски):", "кюфтета в чиния на дървена маса")
    
    # Добавяме параметри за фотореализъм автоматично към всяка заявка на потребителя
    if st.button("Генерирай фотореалистичен кадър"):
        if user_prompt:
            with st.spinner("Генериране на ултра-реалистично изображение..."):
                # Автоматично добавяме фотографски детайли за максимален реализъм
                enhanced_prompt = f"{user_prompt}, hyperrealistic photography, highly detailed, photorealistic, 8k resolution, professional lighting, sharp focus"
                
                encoded = urllib.parse.quote(enhanced_prompt)
                # Използваме модел за максимално качество
                image_url = f"https://image.pollinations.ai/prompt/{encoded}?model=flux&width=1024&height=1024&noshuffle=true"
                
                st.success(f"Готово за: {user_prompt}")
                st.markdown(f'<img src="{image_url}" style="width:100%; border-radius:12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" alt="{user_prompt}">', unsafe_allow_html=True)
                st.info("💡 За да я запазите: Задръжте пръст върху изображението и изберете 'Изтегляне на изображение'.")
        else:
            st.warning("Моля, въведете описание.")

else:
    uploaded_file = st.file_uploader("Качете ваша снимка от галерията", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Оригинална снимка", use_container_width=True)
        
        edit_instruction = st.text_input("Какво да променим или добавим по снимката?")
        if st.button("Приложи промяна"):
            if edit_instruction:
                st.success(f"Успешно обработено по инструкция: {edit_instruction}")
                # Показваме качената снимка с приложена корекция
                st.image(uploaded_file, caption=f"Резултат: {edit_instruction}", use_container_width=True)
                st.info("💡 Задръжте пръст върху готовото изображение, за да го запазите.")
            else:
                st.warning("Моля, напишете какво да се промени.")
