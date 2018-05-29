import kivy
from kivy.app import App
from kivy.uix.label import Label
import arabic_reshaper
from bidi.algorithm import get_display


class FirstApp(App):
     def build(self):
        text = " High Range in case : يزيد عند وجود أمراض فى الكلى مثل الفشل الكلوى"
        reshaped_text = arabic_reshaper.reshape(text=text)
        bidi_text = get_display(reshaped_text)
        return Label(text=bidi_text,font_name= 'Arial')

if __name__ == '__main__':
    FirstApp().run()