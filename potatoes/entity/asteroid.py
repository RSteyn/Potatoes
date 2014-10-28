from ..attributes import Movable, Renderable, Killable
from ..attributes.collidable import Collidable
from .entity import Entity
from ..vector import Vector
from ..values import GAME_WIDTH, GAME_HEIGHT
from random import random, randrange, choice
import math

class Asteroid(Entity, Movable, Renderable, Killable, Collidable):
    MAX_VEL = 100    # TODO: Balance this
    MIN_VEL = 50    # TODO: Balance this
    ACCEL = 125     # TODO: Balance this
    FACE_DICT = {
        'Riley': {'gif': 'riley.gif', 'dimensions': (32, 55)},
        'Nelson': {'gif': 'nelson.gif', 'dimensions': (45, 47)},
        'Theo': {'gif': 'theo.gif', 'dimensions': (36, 55)},
    }

    def __init__(self, state, canvas):
        # Initialise random direction,velocity
        dir = 2*math.pi * random()
        vel = randrange(self.MIN_VEL, self.MAX_VEL)
        # Initialise attributes
        Entity.__init__(self, Vector(0, 0),
                        screen_wrap=True)
        Movable.__init__(self, vel, dir,
                         max_speed=vel,
                         friction=1)
        # Randomise face used
        face_name = choice(list(Asteroid.FACE_DICT.keys()))
        resource = Asteroid.FACE_DICT[face_name]['gif']
        x_dim = Asteroid.FACE_DICT[face_name]['dimensions'][0]
        y_dim = Asteroid.FACE_DICT[face_name]['dimensions'][1]

        Renderable.__init__(self, self.pos, 75, 110,
                            'resources/' + resource, canvas)
        Collidable.__init__(self, self.pos.x, self.pos.y,
                            x_dim, y_dim, canvas)
        Killable.__init__(self, 1)

        # Set asteroid at correct position
        if math.pi/4 > dir > -math.pi/4:
            # Direction in left-quadrant, heading left
            start_pos = Vector(GAME_WIDTH+self.width//2,
                               randrange(GAME_HEIGHT+self.height//2))
        elif 3*math.pi//4 < dir < math.pi or -3*math.pi//4 > dir > -math.pi:
            # Direction in right-quadrant, heading right
            start_pos = Vector(-self.width//2,
                               randrange(GAME_HEIGHT+self.height//2))
        elif math.pi/4 < dir < 3*math.pi//4:
                        # Direction in bottom-quadrant, heading downwards
            start_pos = Vector(randrange(GAME_WIDTH+self.width//2),
                               -self.height//2)
        else:
            # Direction in upper-quadrant, heading upwards
            start_pos = Vector(randrange(GAME_WIDTH+self.width//2),
                               GAME_HEIGHT+self.height//2-1)
        self.pos = start_pos

        self.state = state  # Store reference
    def update(self, delta, gx):
        # Move asteroid
        self.move(delta)
        gx.coords(self.img, (self._pos.x, self._pos.y))
        self.bounding_ellipse.update(gx, self.pos)

        # # Perform asteroid boundary checks.
        # if self.pos.x + self.width//2 <=0 \
        #         or self.pos.x - self.width//2 > GAME_WIDTH:
        #     self.state.remove_asteroid(self)
        # if self.pos.y + self.height//2 <=0 \
        #         or self.pos.y - self.height//2 > GAME_HEIGHT:
        #     self.state.remove_asteroid(self)