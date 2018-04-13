import kivy
from PIL import Image
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from PIL import *
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_string('''

<RootWidget>:
    manager: manager
    img: img
    img3:img3
    img4:img4
    lab:lab
    do_default_tab:false
    ScreenManager:
        id:manager
        Screen:
            id:sc1
            name:"Load Img"
            FilechooserIconView
                canvas.before:
                    Rectangle:
                        pos:self.pos
                        size:self.size
                on_selection:root.select_to(*args)
        Screen:
            id:sc2
            name:"Image"
            FloatLayout:
                Button:
                    id:lab
                    pos_hint:{'right':0.55,'top':1}
                    size_hint:.15,0.1
            RelativeLayout:
                Image:
                    id:img
                    on_touch_down:str('Relative: {}'.format(args[1].pos))
                    pos_hint:{"left":1,'buttom':1}
                    size_hint:0.5,1
                    allow_strech:True
            RelativeLayout:
                Image:
                    id:img3
                    pos_hint:{"right":1,'buttom':1}
                    size_hint:0.5,1
                    allow_strech:True


        Screen:
            id:sc3
            name:"Image_"
            FloatLayout:
                Image:
                    id:img4
                    keep_data:True
                    pos:self.pos
                    size:self.size
    TabbedpanelHeader:
        text:sc1.name
        background_color:1,0,0,1
        screen:sc1.name
    TabbedpanelHeader:
        text:sc2.name
        background_color:1,1,0,1
        screen:sc2.name
    TabbedpanelHeader:
        text:sc3.name
        background_color:1,0,1,1
        screen:sc3.name
''')

class RootWidget(TabbedPanel):
    manager = ObjectProperty(None)
    def on_touch_up(self, touch):
        if not self.img3.collide_point(*touch.pos):
            return True
        else:
            self.lab.text = 'Pos: (%d,%d)' % (touch.x,touch.y)
            return True
    def switch_to(self, header):
        self.manager.current = header.screen
        self.current_tab.state= "normal"
        header.state='down'
        self.current_tab = header
    def select_to(self,*args):
        try:
            print(args[1][0])
            iw = Image.open(args[1][0])
            iw.save('./phase.jpg')
            gray = iw.convert('1')
            gray.save('./gray.jpg')
            self.img.source = './phase.jpg'
            self.img3.source = './gray.jpg'
            self.img4.source = './gray.jpg'
            self.img.reload()
            self.img3.reload()
            self.img4.reload()
        except:
            pass
class MainApp(App):
    title = "screen Widget"
    def build(self):
        return RootWidget()
















