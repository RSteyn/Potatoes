from tkinter import PhotoImage

__author__ = 'rileysteyn'


class Renderable:
    def __init__(self, pos, img_width, img_height, img_path, canvas):
        self.pi = PhotoImage(file=img_path)
        tag = str(self)
        self._img = canvas.create_image(pos.x, pos.y,
                                        image=self.pi,
                                        tag=tag)
        self._width = img_width
        self._height = img_height

    @property
    def img(self):
        return self._img

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def update(self):
        # Really just ensures that the drawn item is now deleted
        self.remove_tag(self._img, 'idle')