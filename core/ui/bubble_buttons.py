# -*- coding: utf-8 -*
from kivy.uix.bubble import Bubble
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

class BaseBubbleButtons(Bubble):

    def __init__(self, **kwargs):
        super(BaseBubbleButtons, self).__init__(**kwargs)

    def hide(self, instance=None, value=None):
        self.opacity = 0

    def show(self, instance=None, value=None):
        self.opacity = 1

class BubbleButtons(Screen,BaseBubbleButtons):
    resize_button = ObjectProperty()
