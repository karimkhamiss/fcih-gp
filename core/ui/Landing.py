from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

# Builder.load_file('Landing.kv')
Config.set('graphics', 'width', '270')
Config.set('graphics', 'height', '460')

class Box(BoxLayout):
    pass
	

class Landing(App):
    def build(self):
        return Box()
		

if __name__ == "__main__":
    Landing().run()
