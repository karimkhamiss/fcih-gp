from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, ListProperty, NumericProperty,StringProperty
from bidi.algorithm import get_display
from core.classifier.prediction import output_his, prediction
from core.postprocessing.finalResult import getTestResult
from kivy.core.window import Window
from core.ui.image_layout import ImageLayout
from core.ui.edit_image_layout import EditImageLayout
from core.ui.bubble_buttons import BubbleButtons
import arabic_reshaper
from db.database import login
from db.database import signup
import sqlite3

Window.size = (280, 500)
sm = ScreenManager()
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
    email_text_input = ObjectProperty()
    password_text_input = ObjectProperty()
    def login(self):
        email = self.email_text_input.text
        password = self.password_text_input.text
        if(len(login(email,password))>0):
            sm.current = 'home'
        else:
            box = BoxLayout(orientation='vertical')
            button = Button(text='Try Again?')
            box.add_widget(Label(text='Wrong Email Or Password'))
            box.add_widget(button)
            popup = Popup(title='Login Status', content=box)
            # popup = Popup(title='Login Status', content=Label(text='Wrong Email Or Password'),
            #               auto_dismiss=False)
            button.bind(on_press=popup.dismiss)
            popup.open()
    pass

class SignUpScreen(Screen):
    male = ObjectProperty(True)
    female = ObjectProperty(False)
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    age_text_input = ObjectProperty()
    email_text_input = ObjectProperty()
    password_text_input = ObjectProperty()
    def signup(self):
        first_name = self.first_name_text_input.text
        last_name = self.last_name_text_input.text
        age = self.age_text_input.text
        email = self.email_text_input.text
        password = self.password_text_input.text
        gender = 1
        signup(first_name, last_name,age,gender,email,password)
        sm.current = 'home'
    pass

class HomeScreen(Screen):
    pass

class CameraScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png("captured.png")

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
class EditImageScreen(Screen):
    NAME_SCREEN = 'crop'

    def __init__(self, **kwargs):
        kwargs.update({'name': self.NAME_SCREEN})
        super(EditImageScreen, self).__init__(**kwargs)
        self.layout = None

    def on_pre_enter(self):
        self.layout = EditImageLayout(sm=sm)
        self.add_widget(self.layout)

presentation = Builder.load_file("main.kv")

class MainApp(App):
    screens = [LandingScreen,SignUpScreen,LoginScreen,HomeScreen,CameraScreen,EditImageScreen,ResultScreen]
    def build(self):
        for class_screen in self.screens:
            sm.add_widget(class_screen())
        return sm
MainApp().run()