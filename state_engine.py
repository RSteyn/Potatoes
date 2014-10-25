from tkinter import *
import time


class StateEngine:
    def __init__(self, game):
        self.states = []
        self.game = game  # Reference

    def change_state(self, state):
        self.states[-1].clean_up()
        self.states[-1] = state(self.game)

    def new_state(self, state):
        if self.states:
            self.states[-1].clean_up()
        self.states.append(state)

    def rem_state(self):
        self.states[-1].clean_up()
        self.states.pop()

    def update(self, delta):
        self.states[-1].update(delta)

    def draw(self):
        self.states[-1].draw()


class State:
    """ This is meant to be a virtual class.  Python does not really
    support this, but making one makes me feel better and allows me
    to create parent-level code if I so wish
    """
    def __init__(self, game):
        self.game = game

    def clean_up(self):
        self.game.reset_frame()

    def update(self, delta):
        pass


class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.cumulative_time = 0 # Holds cumulative time of every update
        self.score = 0
        self.is_ended = False
        self.game.running = True
        self.last_time = time.time()
        self.frames = 0
        self.frame_count = 0

        # Set up widgets
        self.canvas = Canvas(self.game.frame, width=game.width,
                             height=game.height, bg=Game.BACKGROUND_COLOUR,
                             borderwidth=0, highlightthickness=0)
        self.canvas.pack()
        self.game.root.bind("p", self.pause)

    def clean_up(self):
        super().clean_up()
        # Simply goes through events bound and unbinds them
        self.game.root.unbind("<Key-P>")

    def update(self, delta):
        self.canvas.delete("all")
        super().update(delta)
        self.cumulative_time += delta
        self.frames += 1
        # If second has elapsed, get FPS
        if self.cumulative_time > 1:
            self.cumulative_time -= 1
            self.frame_count = self.frames
            self.frames = 0
        self.canvas.create_text(20, 20, text='FPS: ' + str(self.frame_count),
                                font=(Game.FONT, 12),
                                fill=Game.TEXT_COLOUR,
                                anchor=NW)
        if self.game.running:
            pass
            # Resets the canvas to avoid trails.

    # Miscellaneous
    def pause(self, event):
        """ Method to toggle the is_running boolean in the game
        """
        if not self.is_ended:
            self.canvas.create_text(self.game.width // 2,
                                    self.game.height // 2,
                                    text="Paused",
                                    font=(Game.FONT, 50),
                                    fill=Game.TEXT_COLOUR)
            self.game.running = not self.game.running

    # Specific game-related things


class Game:
    # Class variables and methods.
    BACKGROUND_COLOUR = 'black'
    TEXT_COLOUR = "#FFFFFF"
    FONT = "Menlo"
    FONT_SIZE = 15
    TICK_TIME = 16
    FPS = 1 // TICK_TIME

    #==============================#
    # Instance variables and methods
    def __init__(self, width, height):

        # Initialise variables
        self._width = width
        self._height = height
        self.game_mode = ""
        self._running = True
        self.switch_state = None
        self.user_name = "Gardiner"
        self.state_engine = StateEngine(self)
        self.last_update_time = time.time()

        # Create the game window
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", exit)
        self.root.resizable(0, 0)
        self.root.title("Happy Birthday!")

        self.frame = Frame(self.root, width=self._width,
                           height=self._height, bg=Game.BACKGROUND_COLOUR)

        self.frame.pack()

        #  Centers and sizes game window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        win_x = (screen_width - self._width) // 2
        win_y = (screen_height - self._height) // 2
        self.root.geometry("%dx%d+%d+%d" %
                           (self._width, self._height, win_x, win_y))
        self.state_engine.new_state(GameState(self))

        # Get previous high scores, then start game loop
        self.game_loop()
        self.root.mainloop()

    def switch_to_state(self, state):
        """ Simply a setter for the switch_state variable
        """
        self.switch_state = state

    def reset_frame(self):
        """ Used for resetting everything currently on the
        game window.  This is used for switching between states.
        The code is small, but commonly used, so I made it a function.
        """
        if self.frame is not None:
            self.frame.destroy()

        self.frame = Frame(self.root,
                           width=self._width,
                           height=self._height,
                           bg=Game.BACKGROUND_COLOUR)
        self.frame.pack()

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, value):
        self._running = value

    @property
    def mode(self):
        return self.game_mode

    @mode.setter
    def mode(self, value):
        self.game_mode = value

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def name(self):
        return self.user_name

    @name.setter
    def name(self, value):
        self.user_name = value

    def exit(self):
        self.root.destroy()

    # Game loop
    def game_loop(self):
        time_now = time.time()
        if self.switch_state is not None:
            self.state_engine.change_state(self.switch_state)
            self.switch_state = None
        delta = time_now - self.last_update_time
        self.last_update_time = time_now
        self.state_engine.update(delta)
        self.root.after(self.TICK_TIME, self.game_loop)

app = Game(800, 500)
