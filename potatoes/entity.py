from .vector import Vector
from tkinter import *


class Entity:
    def __init__(self):
        self._pos = Vector(0, 0)

    def update(self, delta):
        pass


class Renderable:
    def __init__(self, x, y, img_path, canvas):
        pi = PhotoImage(file=img_path)
        self._img = canvas.create_image(50, 50, image=pi)

    @property
    def img(self):
        return self._img


class Shootable:
    def shoot(self, x, y):
        pass


class Movable:
    def __init__(self):
        self._moving = Vector(0, 0)

    @property
    def moving(self):
        return self._moving

    @moving.setter
    def moving(self, val):
        self._moving = val

    def move(self):
        self._pos += self._moving
