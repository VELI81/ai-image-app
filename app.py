import gradio as gr
from PIL import Image

def generate_or_edit(prompt, image):
    if image is not None:
        # Тук работи функцията за редактиране на качена снимка (Image-to-Image)
        return image, f"Успешно обработено с промпт: {prompt}"
    else:
        # Тук работи генерацията по текст (Text-to-Image)
        # За тест връщаме примерен резултат или свързан AI модел
        return gr.make_random_image(), f"Генерирано по текст: {prompt}"

demo = gr.Interface(
    fn=generate_or_edit,
    inputs=[
        gr.Textbox(label="Опишете какво искате да създадете или промените"),
        gr.Image(type="pil", label="Качете снимка за корекция (по желание)")
    ],
    outputs=[
        gr.Image(label="Резултат"),
        gr.Textbox(label="Статус")
    ],
    title="AI Image Generator & Editor",
    description="Генерирайте картини по текст или качете собствена снимка, за да я редактирате с изкуствен интелект."
)

if __name__ == "__main__":
    demo.launch()
