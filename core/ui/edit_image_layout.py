# -*- coding: utf-8 -*
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from core.ui.bubble_buttons import BubbleButtons
from core.ui.image_layout import ImageLayout
from kivy.uix.button import Button
from  kivy.input import motionevent
from kivy.graphics import Line, Color

up_pos_x = None
up_pos_y = None
down_pos_x = None
down_pos_y = None

class TouchSelector(Widget):
    global down_pos_x, down_pos_y, up_pos_x, up_pos_y
    # Points of Line object
    Ax = NumericProperty(0)
    Ay = NumericProperty(0)
    Bx = NumericProperty(0)
    By = NumericProperty(0)
    Cx = NumericProperty(0)
    Cy = NumericProperty(0)
    Dx = NumericProperty(0)
    Dy = NumericProperty(0)

    # Object line
    line = ObjectProperty()

    # List of line objects drawn
    list_lines_in_image = ListProperty([])

    # Size of the selected rectangle
    size_selected = ListProperty([0, 0])

    # Size previous of the selected rectangle
    size_selected_previous = ListProperty([0, 0])

    # Size temporary of the selected rectangle
    size_selected_temp = ListProperty([0, 0])

    # Line Color and width
    line_color = ListProperty([1, 1, 1, 1])
    line_width = NumericProperty(3)

    # First tap in TouchSelector
    first_tap = True

    def __init__(self, *args, **kwargs):
        super(TouchSelector, self).__init__(*args, **kwargs)
        self.bind(list_lines_in_image=self.remove_old_line)

    def on_touch_up(self, touch):
        self.size_selected = abs(self.Cx - self.Dx), abs(self.Cy - self.By)
        self.size_selected_previous = self.size_selected
        global up_pos_x, up_pos_y
        up_pos_x = touch.x
        up_pos_y = touch.y


    def on_touch_down(self, touch):
        with self.canvas:
            Color(self.line_color)

            # Save initial tap position
            self.Ax, self.Ay = self.first_touch_x, self.first_touch_y = touch.x, touch.y

            # Initilize positions to save
            self.Bx, self.By = 0, 0
            self.Cx, self.Cy = 0, 0
            self.Dx, self.Dy = 0, 0

            # Create initial point with touch x and y postions.
            self.line = Line(points=([self.Ax, self.Ay]), width=self.line_width, joint='miter', joint_precision=30)

            # Save the created line
            self.list_lines_in_image.append(self.line)
            global down_pos_x, down_pos_y
            down_pos_x = touch.x
            down_pos_y = touch.y

    def remove_old_line(self, instance=None, list_lines=None):
        """Remove the old line draw"""
        if len(self.list_lines_in_image) > 1:
            self.delete_line()

    def delete_line(self, pos=0):
        try:
            self.list_lines_in_image.pop(pos).points = []
        except:
            pass

    def on_touch_move(self, touch):
        # Assign the position of the touch at the point C
        self.Cx, self.Cy = touch.x, touch.y

        # There are two known points A (starting point) and C (endpoint)
        # Assign the  positions x and y  known of the points
        self.Bx, self.By = self.Cx, self.Ay
        self.Dx, self.Dy = self.Ax, self.Cy

        # Assign points positions to the last line created
        self.line.points = [self.Ax, self.Ay,
                            self.Bx, self.By,
                            self.Cx, self.Cy,
                            self.Dx, self.Dy,
                            self.Ax, self.Ay]

        self.size_selected_temp = abs(self.Cx - self.Dx), abs(self.Cy - self.By)

    def tap_not_draw_a_line(self):
        """
        When touchdown is called and tap not draw a line.
        """
        return (self.size_selected[0] == 0 and self.size_selected[1] == 0)


class EditImageLayout(Screen):
    global down_pos_x, down_pos_y, up_pos_x, up_pos_y
    color_button = ListProperty([1, .3, .4, 1])
    button_color = ListProperty([0, 0, 0, 1])
    rectangle_selector = ObjectProperty()
    text_size_rectangle = ObjectProperty()
    image_layout = ObjectProperty()
    bubble_buttons = ObjectProperty()

    def __init__(self, **kwargs):
        self.sm = kwargs.pop('sm', None)
        self.crop_image_screen = kwargs.pop('crop_image_screen', None)
        super(EditImageLayout, self).__init__(**kwargs)
        self.rectangle_selector.bind(size_selected=self.on_change_size_rectangle_selector)
        self.rectangle_selector.bind(size_selected_temp=self.update_text_size_rectangle)
        self.bind(on_touch_down=self.bubble_buttons.hide)
        self.bubble_buttons.resize_button.bind(on_press=self.on_press_resize_button)

    def on_change_size_rectangle_selector(self, instance, size_selected):
        if not self.rectangle_selector.tap_not_draw_a_line():
            self.bubble_buttons.show()
        else:
            self.text_size_rectangle.text = ''

    def on_press_resize_button(self, instance):
        global down_pos_x, down_pos_y, up_pos_x, up_pos_y
        self.image_layout.resize_image(width=int(self.rectangle_selector.size_selected[0]),
                                       height=int(self.rectangle_selector.size_selected[1]),
                                       up_pos_x=int(up_pos_x), up_pos_y=int(up_pos_y),
                                       down_pos_x=int(down_pos_x), down_pos_y=int(down_pos_y))

        self.rectangle_selector.delete_line()
        self.text_size_rectangle.text = ''

    def update_text_size_rectangle(self, instance, size):
        self.text_size_rectangle.text = str('({0}, {1})'.format(int(size[0]), int(size[1])))
