from tkinter import PhotoImage

__author__ = 'rileysteyn'


class Renderable:
    def __init__(self, x, y, img_path, canvas):
        self.pi = PhotoImage(file=img_path)
        self._img = canvas.create_image(x, y, image=self.pi)

    @property
    def img(self):
        return self._img