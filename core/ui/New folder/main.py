from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen , FadeTransition
from kivy.properties import ObjectProperty
class MainScreen(Screen):
    pass
class AnotherScreen(Screen):
    pass
class ScreenManagement(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)

presentation = Builder.load_file("screens.kv")

class ScreensApp(App):
    def build(self):
        return presentation

ScreensApp().run()