import streamlit as st
from openai import OpenAI

st.markdown("<h2 style='text-align: center;'>Official AI Image Generator</h2>", unsafe_allow_html=True)
st.write("Студио за генерация на изображения с вашия личен API ключ.")

api_key = st.text_input("Въведете вашия OpenAI API ключ (sk-...):", type="password")
prompt = st.text_input("Въведете подробно описание на изображението:", "красив пейзаж")

if st.button("Генерирай с AI"):
    if not api_key:
        st.warning("Моля, въведете вашия OpenAI API ключ в полето отгоре.")
    elif not prompt:
        st.warning("Моля, въведете описание.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            
            with st.spinner("Изкуственият интелект генерира изображението..."):
                image_url = None
                last_error = None
                
                # Опитваме първо с dall-e-3, а ако ключът го няма, минаваме автоматично на dall-e-2
                for model_name in ["dall-e-3", "dall-e-2"]:
                    try:
                        size_param = "1024x1024" if model_name == "dall-e-3" else "512x512"
                        response = client.images.generate(
                            model=model_name,
                            prompt=prompt,
                            size=size_param,
                            n=1,
                        )
                        image_url = response.data[0].url
                        break
                    except Exception as err:
                        last_error = err
                        continue
                
                if image_url:
                    st.success("Изображението е генерирано успешно!")
                    st.image(image_url, caption=prompt, use_container_width=True)
                    st.info("💡 За да я запазите: Задръжте пръст върху снимката и изберете 'Изтегляне на изображение'.")
                else:
                    st.error(f"Генерирането неуспешно. Грешка от OpenAI: {last_error}")
                
        except Exception as e:
            st.error(f"Възникна грешка при инициализацията: {e}")
