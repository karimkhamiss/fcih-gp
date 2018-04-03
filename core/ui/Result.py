from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

Builder.load_string("""

# Reference Res.py
#: import main Res
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

<ResultScreen>:
    student_list: students_list_view
    BoxLayout:
        orientation: 'vertical'
        spacing:20
        canvas:
            Color:
                rgb: .98, .98, .98,1
            Rectangle:
                size: self.size
        
        #logo 
        Button:
            text: "logo "
            background_normal:''
            background_color:0.2, 0.58, 0.992,1
            foreground_color:0.56,0.75,0.94
            font_size:30
            size_hint: 1, .1
        
        #title
        BoxLayout:
            orientation: 'vertical'
            padding:[20,0,20,0] 
            BoxLayout: 
                size_hint: 1, .08
                orientation: 'vertical'
                Label:
                    text: "Analysis Result "
                    background_color:0, 0, 0,1
                    color :0, 0, 0,1
                    font_size:20
                    size_hint: 1, .5
    
                Label:
                    text: "Complete blood picture"
                    color :0.2, 0.58, 0.992,1
                    font_size:20
                    size_hint: 1, .5

            BoxLayout:
                size_hint: 1, .16
                orientation: 'horizontal'
                

                Button:
                    text: "Name"
                    background_normal:''
                    background_color:0.2, 0.58, 0.992,1
                    foreground_color:0.56,0.75,0.94
                    font_size:20
                    size_hint: .25, .5

                Button:
                    text: "Result"
                    background_normal:''
                    background_color:0.2, 0.58, 0.992,1
                    foreground_color:0.56,0.75,0.94
                    font_size:20
                    size_hint: .25, .5

                Button:
                    text: "Feedback"
                    background_normal:''
                    background_color:0.2, 0.58, 0.992,1
                    foreground_color:0.56,0.75,0.94
                    font_size:20
                    size_hint: .5, .5
            BoxLayout:
                size_hint: 1, .5
                orientation:'horizontal'
                background_normal:''
                background_color:0.2, 0.58, 0.992,1
                foreground_color:0.56,0.75,0.94
                
                
                ListView:
                    size_hint: .25, 1
                    id: students_list_view
                    adapter:
                        ListAdapter(data=["Hemoglobin","MCV","MCH","MCHW","ROW","ROW","ROW","ROW"], cls=main.StudentListButton)
                ListView:
                    id: students_list_view
                    size_hint: .25, 1
                    adapter:
                        ListAdapter(data=["12.9","12.9","12.9","12.9","12.9","12.9","12.9","12.9"], cls=main.StudentListButton)
                ListView:
                    id: students_list_view
                    size_hint: .5, 1
                    adapter:
                        ListAdapter(data=["very good your health is well","very good your health is well","very good your health is well","very good your health is well","very good your health is well","very good your health is well","very good your health is well","very good your health is well"], cls=main.StudentListButton)
                   
            Label:
                text:'Unlike many other toolkits, Each child is automatically assigned a position determined by the layout configuration and the child’s index in the children list.'
                text_size: root.width-100, None
                color :0, 0, 0,1
                font_size:20
                size_hint: 1, .3



        Button:
            size_hint: 1, .1
            background_normal:''
            background_color:0.2, 0.58, 0.992,1
            foreground_color:0.56,0.75,0.94
            text: "Capture another one ?"
            font_size:30
            pos_hint: {"left": 0, "bottom": 0}


""")


class StudentListButton(ListItemButton):
    selected_color:[0, 0, 0, 1]
    deselected_color: [0, 0, 1, 1]
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
    ResultScreenApp().run()





