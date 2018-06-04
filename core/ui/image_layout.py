from kivy.uix.image import Image
from core.ui.image import CoreImage
from kivy.properties import ObjectProperty, StringProperty, ListProperty
import io
import cv2
from kivy.core.window import Window

class ImageLayout(Image):

    image = ObjectProperty()
    path_image = StringProperty('captured.png')
    path_cropped_image = StringProperty('cropped_image.png')
    old_size = ListProperty([0, 0])
    def __init__(self, **kwargs):
        super(ImageLayout, self).__init__(**kwargs)

        # stretch input image
        im = cv2.imread(self.path_image)
        im_height, im_width = im.shape[:2]
        ratio = Window.width / Window.height
        im = cv2.resize(im, (im_width, int(im_width / ratio)), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(self.path_image,im)

        self.image = CoreImage(self.path_image,
                               data=io.BytesIO(open(self.path_image, "rb").read()),
                               ext=self.path_image[self.path_image.rfind('.') + 1::])
        self.source = self.path_image

    def resize_image(self, width, height, up_pos_x, up_pos_y,down_pos_x,down_pos_y):
        pos_x = None
        pos_y = None
        if down_pos_x < up_pos_x and down_pos_y > up_pos_y :
            pos_x = down_pos_x
            pos_y = down_pos_y

        elif down_pos_x < up_pos_x and down_pos_y < up_pos_y :
            pos_x = down_pos_x
            pos_y = up_pos_y

        elif down_pos_x > up_pos_x and down_pos_y < up_pos_y :
            pos_x = up_pos_x
            pos_y = up_pos_y

        elif down_pos_x > up_pos_x and down_pos_y > up_pos_y :
            pos_x = up_pos_x
            pos_y = down_pos_y

        img = cv2.imread(self.path_image)
        im_height, im_width = img.shape[:2]
        height_ratio = im_height/Window.height
        width_ratio = im_width/Window.width
        pos_y = int(abs(Window.height-pos_y))
        h = int(height*height_ratio)
        w = int(width*width_ratio)
        y = int(pos_y*height_ratio)
        x = int(pos_x*width_ratio)
        img = img[y:y+h, x:x+w]
        cv2.imwrite('cropped_image.jpg', img)
