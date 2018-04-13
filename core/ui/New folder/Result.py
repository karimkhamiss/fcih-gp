from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton



class StudentListButton(ListItemButton):
    selected_color = [0, 0, 0, 1]
    deselected_color = [0, 0, 1, 1]
    pass

# Declare both screens
class ResultScreen(Screen):
    ResultData = ObjectProperty()
    ResultData.adapter.data.extend(["Karim Khamiss"])
    ResultData._trigger_reset_populate()
    pass


class ResultScreenApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(ResultScreen(name='Result'))  # use name to move from screen to another
        return sm


if __name__ == '__main__':
    ResultScreenApp().run()





