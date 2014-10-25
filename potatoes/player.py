from . import attributes as attr


class Player(attr.Movable, attr.Renderable, attr.Shootable):
    def __init__(self):
        super().__init__()
