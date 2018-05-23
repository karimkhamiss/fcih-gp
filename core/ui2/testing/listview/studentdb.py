from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton


class StudentListButton(ListItemButton):
    pass
class StudentDB(BoxLayout):
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    first_col = ObjectProperty()
    seoncd_col = ObjectProperty()
    third_col = ObjectProperty()
    def submit_student(self):
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
        self.student_list.adapter.data.extend([student_name],[student_name])
        self.student_list._trigger_reset_populate()
class StudentDBApp(App):
    def build(self):
        return StudentDB()
dbApp = StudentDBApp().run()