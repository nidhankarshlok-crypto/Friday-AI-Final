from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivy.clock import Clock # UI update sathi mahatvache
from groq import Groq
import threading
import speech_recognition as sr
import pyttsx3

Window.size = (400, 650)

class CoderApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        
        # BRAIN SETUP - Navin Model Model Update kela ahe
        self.api_key = "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"
        self.client = Groq(api_key=self.api_key)
        self.engine = pyttsx3.init()
        
        root_layout = MDBoxLayout(orientation='vertical', padding=10, spacing=5)
        
        header = MDLabel(
            text="CODER: FRIDAY", 
            halign="center", font_style="H5", size_hint_y=0.1,
            theme_text_color="Custom", text_color=(0, 0.9, 1, 1)
        )
        
        self.scroll = MDScrollView()
        self.chat_list = MDBoxLayout(orientation='vertical', size_hint_y=None, spacing=15, padding=10)
        self.chat_list.bind(minimum_height=self.chat_list.setter('height'))
        self.scroll.add_widget(self.chat_list)
        
        input_area = MDBoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=5)
        self.text_input = MDTextField(hint_text="Friday la sang...", mode="round", size_hint_x=0.7)
        
        send_btn = MDIconButton(icon="send", on_release=self.send_text_msg)
        mic_btn = MDIconButton(icon="microphone", on_release=self.start_voice_thread)
        
        input_area.add_widget(self.text_input)
        input_area.add_widget(send_btn)
        input_area.add_widget(mic_btn)
        
        root_layout.add_widget(header)
        root_layout.add_widget(self.scroll)
        root_layout.add_widget(input_area)
        
        # UI safe method ne message add karne
        Clock.schedule_once(lambda dt: self.add_message("Friday", "Online and Ready, sir."))
        
        return root_layout

    def add_message(self, sender, text):
        # He function 'Main Thread' var run hote (Safe for Kivy)
        msg_label = MDLabel(
            text=f"[b]{sender}:[/b] {text}",
            markup=True, size_hint_y=None, theme_text_color="Custom",
            text_color=(0, 0.9, 1, 1) if sender == "Friday" else (1, 1, 1, 1)
        )
        msg_label.bind(texture_size=msg_label.setter('size'))
        self.chat_list.add_widget(msg_label)
        self.scroll.scroll_y = 0

    def send_text_msg(self, instance):
        query = self.text_input.text
        if query:
            self.add_message("Tu", query)
            self.text_input.text = ""
            threading.Thread(target=self.process_ai_task, args=(query,)).start()

    def start_voice_thread(self, instance):
        threading.Thread(target=self.voice_task).start()

    def voice_task(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            Clock.schedule_once(lambda dt: self.add_message("System", "Listening..."))
            try:
                audio = r.listen(source, timeout=5)
                query = r.recognize_google(audio)
                Clock.schedule_once(lambda dt: self.add_message("Tu", query))
                self.process_ai_task(query)
            except:
                Clock.schedule_once(lambda dt: self.add_message("Friday", "Sorry, aikalo nahi."))

    def process_ai_task(self, query):
        try:
            # NAVIN MODEL: llama-3.3-70b-versatile
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "Tu 'Friday' AI ahes. World-class coder."},
                          {"role": "user", "content": query}]
            )
            response = completion.choices[0].message.content
            
            # UI update via Clock (Important!)
            Clock.schedule_once(lambda dt: self.add_message("Friday", response))
            
            self.engine.say(response)
            self.engine.runAndWait()
        except Exception as e:
            error_msg = str(e)
            Clock.schedule_once(lambda dt: self.add_message("Error", error_msg))

if __name__ == "__main__":
    CoderApp().run()