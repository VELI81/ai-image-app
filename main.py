import requests
import urllib.parse
import base64
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from plyer import filechooser

class AIImageApp(App):
    def build(self):
        self.selected_image_path = None
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text="AI Генератор & Редактор на снимки", size_hint=(1, 0.08))
        self.layout.add_widget(self.label)
        
        self.txt_prompt = TextInput(hint_text="Опиши снимката или промяната...", size_hint=(1, 0.12), multiline=False)
        self.layout.add_widget(self.txt_prompt)
        
        btn_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.12), spacing=10)
        
        self.btn_select = Button(text="📁 Избери снимка", background_color=(0.5, 0.5, 0.5, 1))
        self.btn_select.bind(on_press=self.open_gallery)
        btn_layout.add_widget(self.btn_select)
        
        self.btn_generate = Button(text="✨ Създай / Промени", background_color=(0.2, 0.6, 1, 1))
        self.btn_generate.bind(on_press=self.process_image)
        btn_layout.add_widget(self.btn_generate)
        
        self.layout.add_widget(btn_layout)
        
        self.img_result = AsyncImage(size_hint=(1, 0.68))
        self.layout.add_widget(self.img_result)
        
        return self.layout

    def open_gallery(self, instance):
        filechooser.open_file(on_selection=self.on_file_selected, filters=[("Images", "*.png", "*.jpg", "*.jpeg")])

    def on_file_selected(self, selection):
        if selection:
            self.selected_image_path = selection[0]
            self.btn_select.text = "✅ Избрана снимка"
            self.img_result.source = self.selected_image_path
            self.img_result.reload()

    def process_image(self, instance):
        prompt = self.txt_prompt.text
        if not prompt and not self.selected_image_path:
            return
            
        encoded_prompt = urllib.parse.quote(prompt if prompt else "enhance image")
        
        # Ако има избрана лична снимка -> правим промяна по нея
        if self.selected_image_path:
            try:
                with open(self.selected_image_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                url = f" https://image.pollinations.ai/prompt/{encoded_prompt}?image={encoded_string}&width=1024&height=1024&nologo=true"
            except Exception as e:
                url = f" https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
        else:
            # Ако няма избрана снимка -> генерираме нова от нулата
            url = f" https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
            
        self.img_result.source = url
        self.img_result.reload()

if __name__ == '__main__':
    AIImageApp().run()
