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

from core.ui.navigationdrawer import NavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar, ActionButton, ActionPrevious
from kivy.properties import  ObjectProperty
from core.classifier.prediction import output_his, prediction

Config.set('graphics', 'width', '440')
Config.set('graphics', 'height', '620')
### Menu ###
SidePanel_AppMenu = {'Home':['Press_Home',None],
                     'My Analysis':['Press_Analysis',None],
                     'Profile':['Press_Profile',None],
                     'Legal&Privacy':['Press_Legal',None],
                     'Setting':['Press_Setting',None],
                     }
id_AppMenu_METHOD = 0
id_AppMenu_PANEL = 1
RootApp = None

class SidePanel(BoxLayout):
    pass

class MenuItem(Button):
    def __init__(self, **kwargs):
        super(MenuItem, self).__init__( **kwargs)
        self.bind(on_press=self.menuitem_selected)

    def menuitem_selected(self, *args):
        print (self.text, SidePanel_AppMenu[self.text], SidePanel_AppMenu[self.text][id_AppMenu_METHOD])
        try:
            function_to_call = SidePanel_AppMenu[self.text][id_AppMenu_METHOD]
        except:
            print ('error')
            return
        getattr( RootApp, function_to_call )()



class AppActionBar(ActionBar):
    pass

class ActionMenu(ActionPrevious):
    def menu(self):
        print ('ActionMenu')
        RootApp.toggle_sidepanel()



class MainPanel(BoxLayout):
    pass

class AppArea(FloatLayout):
    pass

class CircularButton(ButtonBehavior, Widget):
    pass

class B_Home(FloatLayout):
    pass

class B_Analysis(FloatLayout):
    pass

class B_Profile(FloatLayout):
    pass


class B_Legal(FloatLayout):
    pass


class B_Setting(FloatLayout):
    pass




class NavDrawer(NavigationDrawer):
    def __init__(self, **kwargs):
        super(NavDrawer, self).__init__( **kwargs)

    def close_sidepanel(self, animate=True):
        if self.state == 'open':
            if animate:
                self.anim_to_state('closed')
            else:
                self.state = 'closed'

# presentation = Builder.load_file("androidapp.kv")


class Menu(App):

    def build(self):
        global RootApp
        RootApp = self

        # NavigationDrawer
        self.navigationdrawer = NavDrawer()

        # SidePanel
        side_panel = SidePanel()
        self.navigationdrawer.add_widget(side_panel)

        # MainPanel
        self.main_panel = MainPanel()
        self.navigationdrawer.anim_type = 'slide_above_anim'
        self.navigationdrawer.add_widget(self.main_panel)

        return self.navigationdrawer

    def toggle_sidepanel(self):
        self.navigationdrawer.toggle_state()

    def Press_Home(self):
        print ('Home')

    def Press_Analysis(self):
        print ('Analysis')
        self._switch_main_page('My Analysis', B_Analysis)


    def Press_Profile(self):
        print ('Profile')
        self._switch_main_page('Profile',  B_Profile)


    def Press_Legal(self):
        print ('Legal')
        self._switch_main_page('Legal&Privacy',  B_Legal)


    def Press_Setting(self):
        print ('Profile')
        self._switch_main_page('Setting',  B_Setting)

    def _switch_main_page(self, key,  panel):
        self.navigationdrawer.close_sidepanel()

        if not SidePanel_AppMenu[key][id_AppMenu_PANEL]:
            SidePanel_AppMenu[key][id_AppMenu_PANEL] = panel()

        main_panel = SidePanel_AppMenu[key][id_AppMenu_PANEL]
        self.navigationdrawer.remove_widget(self.main_panel)
        self.navigationdrawer.add_widget(main_panel)
        self.main_panel = main_panel

### Menu ###
class Box(BoxLayout):
    def predict(self):
        List = []
        List = output_his()  # return list of vectors in  each image but in list
        linelist = prediction(List)
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
class StudentListButton(ListItemButton):
    selected_color = [0, 0, 0, 1]
    deselected_color = [0, 0, 1, 1]
    pass


# Declare both screens
class ResultScreen(Screen):
    pass

class ResultScreenApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(ResultScreen(name='Result'))  # use name to move from screen to another
        return sm

if __name__ == '__main__':
    List = []
    item=["MCH","20","Clinical chemistry","يزيد عند مرض النقرص"]
    List.append(item)
    for item in List:
        print(item[0])
    Landing().run()
    Home().run()
    LoginApp().run()
    SignUpApp().run()
    Menu().run()
    ResultScreenApp().run()