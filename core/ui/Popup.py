from kivy import platform, require
require('1.9.0')
from kivy.app import App
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
class MainPopup(ModalView):
    def __init__(self, title, txt,button, callback=None, alpha=0.8,
                 width=None, height=None, **kwargs):
        super(MainPopup, self).__init__(**kwargs)

        self.callback = callback
        self.auto_dismiss = False
        self.background = "dlgback_green.png"
        self.background_color = (0, 0, 0, alpha)
        self.size_hint = (None, None)
        self.preferred_width = width
        self.preferred_height = height

        if self.preferred_width:
            self.width = self.preferred_width
        elif Window.width > 500:  # Big screen?
            self.width = 0.7 * Window.width
        else:
            self.width = Window.width - 2

        self.playout = BoxLayout(orientation='vertical',
                                 padding=["2dp", "5dp",
                                          "2dp", "5dp"],
                                 spacing="5dp")

        self.title = Label(size_hint_y=None,
                           text_size=(self.width - dp(20), None),
                           text=title,
                           halign='left',
                           font_size="16sp",
                           color=(0.2,0.58,0.992,1),
                           markup=True)

        self.separator = BoxLayout(size_hint_y=None, height="1dp")

        self.pscroll = ScrollView(do_scroll_x=False)

        self.content = Label(size_hint_y=None,
                             text=txt,
                             halign='justify',
                             font_size="16sp",
                             markup=True,
                             color=(0, 0, 0, 1),
                             text_size=(self.width - dp(20), None))
        # text: "Sign Up"
        # pos_hint: {"center_x": .5, "top": .28}
        # size_hint: .3, .1
        # background_normal: ''
        # background_color: 0.2, 0.58, 0.992, 1
        self.pbutton = Button(text=button,
                              background_color=(0.2,0.58,0.992,1),
                              size_hint_y=None, height="25dp",
                              )
        self.pbutton.bind(on_release=self.close)

        self.add_widget(self.playout)
        self.playout.add_widget(self.title)
        self.playout.add_widget(self.separator)
        self.playout.add_widget(self.pscroll)
        self.pscroll.add_widget(self.content)
        self.playout.add_widget(self.pbutton)

        self.title.bind(texture_size=self.update_height)
        self.content.bind(texture_size=self.update_height)

        with self.separator.canvas.before:
            Color(0.7,0.7,0.7, 1)
            self.rect = Rectangle(pos=self.separator.pos,
                                  size=self.separator.size)

        self.separator.bind(pos=self.update_sep,
                            size=self.update_sep)

        Window.bind(size=self.update_width)

        self.open()

    def update_width(self, *args):
        # hack to resize dark background on window resize
        self.center = Window.center
        self._window = None
        self._window = Window

        if self.preferred_width:
            self.width = self.preferred_width
        elif Window.width > 500:  # Big screen?
            self.width = 0.7 * Window.width
        else:
            self.width = Window.width - 2

        self.title.text_size = (self.width - dp(20), None)
        self.content.text_size = (self.width - dp(20), None)

    def update_height(self, *args):
        self.title.height = self.title.texture_size[1]
        self.content.height = self.content.texture_size[1]
        temp = self.title.height + self.content.height + dp(56)
        if self.preferred_height:
            self.height = self.preferred_height
        elif temp > Window.height - dp(40):
            self.height = Window.height - dp(40)
        else:
            self.height = temp
        self.center = Window.center

    def update_sep(self, *args):
        self.rect.pos = self.separator.pos
        self.rect.size = self.separator.size

    def close(self, instance):
        self.dismiss(force=True)
        if self.callback:
            self.callback()
class TestApp(App):
    def build(self):
       return MainPopup(title="Login Status", txt="Wrong Username Or Password", button="Try Again", width=None, height=None)

    def callback(self):
        exit()

# TestApp().run()