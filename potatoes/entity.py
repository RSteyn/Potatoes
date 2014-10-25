from .vector import Vector
from tkinter import *


class Entity:
    def __init__(self):
        self._pos = Vector(0, 0)

    def update(self, delta, gx):
        pass


class Renderable:
    def __init__(self, x, y, img_path, canvas):
        self.pi = PhotoImage(file=img_path)
        self._img = canvas.create_image(x, y, image=self.pi)

    @property
    def img(self):
        return self._img


class Shootable:
    def shoot(self, x, y):
        pass


class Movable:
    def __init__(self):
        self._moving = Vector(0, 0, polar=True)
        self._direction = 0

    @property
    def velocity(self):
        return self._moving.magnitude

    @velocity.setter
    def velocity(self, val):
        self._moving = Vector(val, self._direction, polar=True)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, val):
        self._direction = val
        self._moving = Vector(self._moving.magnitude, val, polar=True)

    def rotate(self, theta):
        self._moving = self._moving.rotate(theta)
        if theta != 0:
            self._direction = self._moving.direction

    def move(self):
        self._pos += self._moving
