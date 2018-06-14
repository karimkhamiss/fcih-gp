from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, ListProperty, NumericProperty,StringProperty
from bidi.algorithm import get_display
from kivy.uix.scrollview import ScrollView

from core.Validation import validation
from core.classifier.prediction import output_his, prediction
from core.postprocessing.finalResult import getTestResult
from kivy.core.window import Window
from core.ui.image_layout import ImageLayout
from core.ui.edit_image_layout import EditImageLayout
from core.ui.bubble_buttons import BubbleButtons
import arabic_reshaper
from core.db.database import login
from core.db.database import logout
from core.db.database import signup
from core.db.database import get_current_user
from core.db.database import get_test_name
from core.db.database import save_test
from core.db.database import get_medical_history_category
# from core.db.database import set_medical_histories
from core.db.database import get_medical_history_test
from core.ui.Popup import MainPopup
import time
import sqlite3

Window.size = (308, 550)
sm = ScreenManager()
class ListItem(ListItemButton):
    background_normal = ''
    background_color = (.8, .89, 1, 1)
    color = (0.45, 0.45, 0.45, 1)
    font_name = "Arial"
    pass
class Listview1(ListItemButton):
    background_normal = ''
    background_color = (.8, .89, 1, 1)
    color = (0.25, 0.25, 0.25, 1)
    text_size = (int((Window.width-50)*.25), None)
    font_name = "Arial"
    pass
class Listview2(ListItemButton):
    background_normal = ''
    background_color = (.8, .89, 1, 1)
    color = (0.25, 0.25, 0.25, 1)
    text_size = (int((Window.width-50)*.2), None)
    font_name = "Arial"
    pass
class Listview3(ListItemButton):
    background_normal = ''
    background_color = (.8, .89, 1, 1)
    color = (0.25, 0.25, 0.25, 1)
    text_size = (int((Window.width-50)*.55), None)
    font_name = "Arial"
    pass
class LandingScreen(Screen):
    def on_enter(self, *args):
        if get_current_user().id:
            global flag
            flag = True
            logout()
    pass
class LoginScreen(Screen):
    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()
    def on_leave(self, *args):
        self.username_text_input.text =""
        self.password_text_input.text =""
    def login(self):
        username = self.username_text_input.text
        password = self.password_text_input.text
        login_inputs_flag = 1
        if(validation.check_empty(username) or validation.check_empty(password) ):
            login_inputs_flag = 0
            MainPopup(title="Empty Fields",txt="Please fill all fields",button="Try Again?",width=None, height=None)
        elif(not validation.check_name(username)):
            login_inputs_flag = 0
            MainPopup(title="Invalid Username",txt="Username must be started with a letter",button="Try Again?",width=None, height=None)
        if(login_inputs_flag):
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
    def on_leave(self, *args):
        self.first_name_text_input.text = ""
        self.last_name_text_input.text = ""
        self.birthdate_text_input.text = ""
        self.username_text_input.text = ""
        self.password_text_input.text = ""
    def signup(self):
        gender = 1
        if self.female_check_box.active:
           gender = 2
        first_name = self.first_name_text_input.text
        last_name = self.last_name_text_input.text
        birthdate = self.birthdate_text_input.text
        username = self.username_text_input.text
        password = self.password_text_input.text
        signup_inputs_flag = 1
        if(validation.check_empty(first_name) or validation.check_empty(last_name) or
                validation.check_empty(birthdate) or validation.check_empty(username) or validation.check_empty(password)):
            signup_inputs_flag = 0
            MainPopup(title="Empty Fields",txt="Please fill all fields",button="Try Again?",width=None, height=None)
        elif(not validation.check_name(first_name) or not validation.check_name(last_name) or
                not validation.check_name(username)):
            signup_inputs_flag = 0
            MainPopup(title="Invalid Name",txt="Name must be started with a letter",button="Try Again?",width=None, height=None)
        elif(not validation.check_date(birthdate)):
            signup_inputs_flag = 0
            MainPopup(title="Invalid Birthdate",txt="Birthdate must be in this format day/month/year",button="Try Again?",width=None, height=None)
        if(signup_inputs_flag):
            signup(first_name, last_name,birthdate,gender,username,password)
            sm.current = 'home'
    pass
class HomeScreen(Screen):
    username = ObjectProperty()
    def on_enter(self, *args):
        self.username.text = "Welcome , "+get_current_user().first_name+" "+get_current_user().last_name
    pass

class HowToCropScreen(Screen):
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
    def open_popup(self):
        box = BoxLayout(orientation='vertical')
        image = Image(source='..\..\\resources\\ui\\loading.gif')
        box.add_widget(Label(text='Please Wait'))
        box.add_widget(image)
        popup = Popup(title='', separator_height=0, content=box,auto_dismiss=False)
        popup.open()
    def analysis(self):
        tests_values = []
        tests_descriptions = []
        tests = []
        List = output_his()  # return list of vectors in  each image but in list
        linelist = prediction(List)
        print(linelist)
        counter = 0
        self.title.text = linelist[0][0].upper()
        self.first_list.adapter.data = []
        self.second_list.adapter.data = []
        self.third_list.adapter.data = []
        for test_name in linelist[0]:
            counter = counter+1
            if(counter == 1 or test_name == "not matched"):
                continue
            tests.append([test_name,"",""])
            # tests_names.append(test_name)
            self.first_list.adapter.data.extend([test_name])
            self.first_list._trigger_reset_populate()
        for test_value in linelist[2]:
            if (test_value == "none"):
                continue
            tests[len(tests_values)][1] = test_value
            tests_values.append(test_value)
            self.second_list.adapter.data.extend([test_value])
            self.second_list._trigger_reset_populate()
        feedback = getTestResult(linelist, get_current_user().age,get_current_user().gender)
        for test_feedback in feedback:
            tests[len(tests_descriptions)][2] = test_feedback
            tests_descriptions.append(test_feedback)
            reshaped_text = arabic_reshaper.reshape(text=test_feedback)
            unicode_text = get_display(reshaped_text)
            self.third_list.adapter.data.extend([unicode_text])
            self.third_list._trigger_reset_populate()
        save_test(linelist[0][0],tests)
    def on_enter(self, *args):
        self.analysis()
flag = True
class MedicalHistoryScreen(Screen):
    scroll = ScrollView(size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
    def view_result(self,medical_history_id):
        tests = get_medical_history_test(medical_history_id)
        HistoryResultScreen.set_tests(self,tests,medical_history_id)
        # tests_to_view = get_medical_history_test(medical_history_id)
        sm.current = 'history_result'
    def on_enter(self):
        root = self.ids.grid
        root.clear_widgets()
        global flag
        medical_histories = get_current_user().medical_histories
        if flag:
            # create a grid layout
            layout = GridLayout(cols=1, padding=10, spacing=10,
                                size_hint=(1, None))
            layout.bind(minimum_height=layout.setter('height'))
            # add button into that grid
            counter = 0
            for medical_history in medical_histories:
                btn = Button(
                    id=str(medical_history[0])
                    ,text= medical_history[1] + " , " + medical_history[2] , size_hint=(.3, None), height=32
                    , background_normal='', background_color=(.95, .95, .95, 1), color=(.45,.45,.45,1))
                btn.bind(on_press=lambda x: self.view_result(medical_history[0]))
                layout.add_widget(btn)
                counter = counter+1
            # create a scroll view
            scroll = ScrollView(size_hint=(1, 1), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
            scroll.add_widget(layout)
            root = self.ids.grid
            root.add_widget(scroll)
            flag = False
            return root
class HistoryResultScreen(Screen):
    title = ObjectProperty()
    tests_to_view = []
    medical_history_id = 0
    def set_tests(self,tests,id):
        HistoryResultScreen.tests_to_view = tests
        HistoryResultScreen.medical_history_id = id
    def view_result(self):
        self.title.text = get_medical_history_category(self.medical_history_id).upper()
        test_ids = []
        test_names = []
        test_values = []
        test_descriptions = []
        self.first_list.adapter.data=[]
        self.second_list.adapter.data=[]
        self.third_list.adapter.data=[]
        for test in self.tests_to_view:
            test_names.append(get_test_name(test[0]))
            test_values.append(test[1])
            test_descriptions.append(test[2])
        for test_name in test_names:
            self.first_list.adapter.data.extend([test_name])
            self.first_list._trigger_reset_populate()
        for test_value in test_values:
            self.second_list.adapter.data.extend([test_value])
            self.second_list._trigger_reset_populate()
        for test_description in test_descriptions:
            reshaped_text = arabic_reshaper.reshape(text=test_description)
            unicode_text = get_display(reshaped_text)
            self.third_list.adapter.data.extend([unicode_text])
            self.third_list._trigger_reset_populate()
    def on_enter(self, *args):
        self.view_result()
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
    screens = [LandingScreen,SignUpScreen,LoginScreen,HomeScreen,HowToCropScreen,CameraScreen,EditImageScreen,ResultScreen,MedicalHistoryScreen,HistoryResultScreen]
    def build(self):
        for class_screen in self.screens:
            sm.add_widget(class_screen())
        return sm
MainApp().run()