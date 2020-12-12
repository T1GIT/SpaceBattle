from components.overlay import Overlay
from config import Configuration as Conf
from elements.meteor import Meteor
from elements.rocket import Rocket


class Game:
    def __init__(self, window):
        # Environment
        self.window = window
        self.counter_meteors = 0
        self.events = []
        # Initialisation

        # Components
        self.comp_overlay = Overlay(self)
        # TODO: Artem

    def reset(self):
        """
        Erases all mobs and objects
        """
        self.window.sprites.empty()

    def start(self):
        """
        Starts the game
        """
        self.window.sprites.add(Meteor(self))
        # TODO: Artem

    def loop(self):
        """
        Do all actions per one frame
        """
        self.counter_meteors += 1
        if self.counter_meteors == Conf.Window.FPS * 5:
            self.counter_meteors = 0
            self.window.sprites.add(Meteor(self))
        self.window.sprites.update()
        # TODO: Artem
