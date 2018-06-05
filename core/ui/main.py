from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
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
from core.db.database import login
from core.db.database import signup
from core.db.database import get_gender_type
from core.db.database import get_age
from core.ui.Popup import MainPopup
import time
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
    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()
    def login(self):
        username = self.username_text_input.text
        password = self.password_text_input.text
        # sm.current = 'home'
        if(len(login(username,password))>0):
            sm.current = 'home'
        else:
            MainPopup(title="Login Status",txt="Wrong Username Or Password",button="Try Again",width=None, height=None)
    pass

class SignUpScreen(Screen):
    male_check_box = ObjectProperty(None)
    female_check_box = ObjectProperty(None)
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    birthdate_text_input = ObjectProperty()
    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()
    def signup(self):
        gender = 1
        if self.female_check_box.active:
           gender = 2
        first_name = self.first_name_text_input.text
        last_name = self.last_name_text_input.text
        birthdate = self.birthdate_text_input.text
        username = self.username_text_input.text
        password = self.password_text_input.text
        signup(first_name, last_name,birthdate,gender,username,password)
        sm.current = 'home'
    pass

class HomeScreen(Screen):
    pass

class CameraScreen(Screen):
    def open_camera(self):
        camera = self.ids['camera']
        camera.play = True
    def close_camera(self):
        camera = self.ids['camera']
        camera.play = False
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png("captured.png")
        sm.current = "crop"
    def on_enter(self, *args):
        self.open_camera()

class ResultScreen(Screen):
    title = ObjectProperty()
    first_list = ObjectProperty()
    seoncd_list = ObjectProperty()
    third_list = ObjectProperty()
    def open_popup(self):
        box = BoxLayout(orientation='vertical')
        image = Image(source='..\..\\resources\\ui\\loading.gif')
        box.add_widget(Label(text='Please Wait'))
        box.add_widget(image)
        popup = Popup(title='', separator_height=0, content=box,auto_dismiss=False)
        popup.open()
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
        feedback = getTestResult(linelist, get_age(),get_gender_type())
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