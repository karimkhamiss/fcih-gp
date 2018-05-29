from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import  ObjectProperty
import arabic_reshaper
from bidi.algorithm import get_display


from core.classifier.prediction import output_his, prediction
from core.postprocessing.finalResult import getTestResult


class StudentListButton(ListItemButton):
    selected_color = [0, 0, 0, 1]
    deselected_color = [0, 0, 1, 1]
    font_name = "Arial"
    pass

class FeedbackLabel(Label):
    font_name = "Arial"
    pass

class LandingScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    male = ObjectProperty(True)
    female = ObjectProperty(False)
    pass

class HomeScreen(Screen):
    pass

class ResultScreen(Screen):
    title = ObjectProperty()
    first_list = ObjectProperty()
    seoncd_list = ObjectProperty()
    third_list = ObjectProperty()
    def analysis(self):
        List = []
        List = output_his()  # return list of vectors in  each image but in list
        linelist = prediction(List)
        print(linelist)
        counter = 0
        self.title.text = linelist[0][0]
        for test_name in linelist[0]:
            counter = counter+1
            if(counter == 1 or test_name == "not matched"):
                continue
            self.first_list.adapter.data.extend([test_name])
            self.first_list._trigger_reset_populate()
        for test_value in linelist[2]:
            if (test_value == "none"):
                continue
            self.second_list.adapter.data.extend([test_value])
            self.second_list._trigger_reset_populate()
        feedback = getTestResult(linelist, 12, "male")
        for test_feedback in feedback:
            reshaped_text = arabic_reshaper.reshape(text=test_feedback)
            unicode_text = get_display(reshaped_text)
            self.third_list.adapter.data.extend([unicode_text])
            self.third_list._trigger_reset_populate()
    def on_enter(self, *args):
        self.analysis()

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        pass
MainApp().run()