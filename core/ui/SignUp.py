import kivy
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.10.0")

from kivy.app import App


class SUBoxLayout(BoxLayout):

    male = ObjectProperty(True)
    female = ObjectProperty(False)

    pass



class SignUpApp(App):
    def build(self):
        return  SUBoxLayout()


suApp = SignUpApp()
suApp.run()