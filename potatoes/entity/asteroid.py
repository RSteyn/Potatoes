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
        'Edward': {'gif': 'edward.gif', 'dimensions': (46, 55)}
    }

    def __init__(self, state, canvas, pos=None, size=3, direction=None):
        # Initialise random direction,velocity
        if direction is None:
            dir = 2*math.pi * random()
        else:
            dir = direction
        vel = randrange(self.MIN_VEL, self.MAX_VEL)
        # Initialise attributes
        Entity.__init__(self, state,
                        Vector(0, 0),
                        screen_wrap=True)
        Movable.__init__(self, vel, dir,
                         max_speed=vel,
                         friction=1)
        if size == 3:
            Renderable.__init__(self, self.pos, 110, 110,
                                'resources/love_potato.gif', canvas)
            Collidable.__init__(self, self.pos, 110, 110, canvas)
        elif size == 2:
            # Randomise face used
            face_name = choice(list(Asteroid.FACE_DICT.keys()))
            resource = Asteroid.FACE_DICT[face_name]['gif']
            x_dim = Asteroid.FACE_DICT[face_name]['dimensions'][0]
            y_dim = Asteroid.FACE_DICT[face_name]['dimensions'][1]

            Renderable.__init__(self, self.pos, 75, 110,
                                'resources/' + resource, canvas)
            Collidable.__init__(self, self.pos,
                                x_dim, y_dim, canvas)
        else:
            Renderable.__init__(self, self.pos, 30, 42,
                                'resources/potato_chip.gif', canvas)
            Collidable.__init__(self, self.pos, 30, 42, canvas)
        Killable.__init__(self, 1)

        self.size = size
        if pos is None:
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
        else:
            self.pos = pos

    def update(self, delta, gx):
        Renderable.update(self)
        # Move asteroid
        self.move(delta)
        gx.coords(self.img, (self._pos.x, self._pos.y))
        self.bounding_ellipse.update(gx, self.pos)

    def collide_with_bullet(self, bullet):
        bullet_dir = bullet.direction
        if self.size > 1:
            # Spawn smaller asteroids
            for i in range(self.size):
                rand_dir = random() * math.pi/4
                new_dir = bullet_dir + rand_dir
                self.state.spawn_asteroid(direction=new_dir, size=self.size-1,
                                          pos=self.pos)
        self.destroy()

    def destroy(self):
        self.state.canvas.delete(str(self.bounding_ellipse))
        self.state.canvas.delete(str(self))
        self.state.remove_asteroid(self)