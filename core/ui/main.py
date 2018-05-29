import kivy
from kivy import Config
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.app import App
from kivy.uix.widget import Widget

from core.postprocessing.finalResult import getTestResult
# from core.postprocessing.postproccessing import Test
from core.ui.navigationdrawer import NavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar, ActionButton, ActionPrevious
from kivy.properties import  ObjectProperty
# from core.classifier.prediction import output_his, prediction

Config.set('graphics', 'width', '440')
Config.set('graphics', 'height', '620')
class Box(BoxLayout):
    # def predict(self):
    #     List = []
    #     List = output_his()  # return list of vectors in  each image but in list
    #     linelist = prediction(List)
    pass

class Landing(App):
    def build(self):
        return Box()

class SUBoxLayout(BoxLayout):
    male = ObjectProperty(True)
    female = ObjectProperty(False)
    pass

class LoginApp(App):
  pass

class SignUpApp(App):
    def build(self):
        return SUBoxLayout()

class Home(App):
    def build(self):
        return Box()
if __name__ == '__main__':
    # List = []
    # item=["MCH","20","Clinical chemistry","يزيد عند مرض النقرص"]
    # List.append(item)
    # for item in List:
    #     print(item[0])
    # Landing().run()
    # Home().run()
    # LoginApp().run()
    SignUpApp().run()
    # Menu().run()
    # ResultScreenApp().run()