import pygame as pg

from managers.sound import Sound
from managers.image import Image
from components.game import Game
from components.menu import Menu
from managers.config import Configuration as Conf


class Window:
    def __init__(self):
        # Environment
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        self.running = True
        # Initialisation
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(Conf.Window.TITLE)
        self.screen = pg.display.set_mode((Conf.Window.WIDTH, Conf.Window.HEIGHT))
        # Managers
        self.mngr_sound = Sound(self)
        self.mngr_image = Image(self)
        # Components
        self.comp_game = Game(self)
        self.comp_menu = Menu(self)

    def reset(self):
        """
        Reloads the game and opens the menu
        """
        self.comp_game.reset()
        self.comp_menu.reset()
        self.sprites = pg.sprite.Group()

    def start(self):
        """
        Starts the game
        """
        self.comp_game.start()
        self.comp_menu.hide()

    def keyboard_listener(self, event: pg.event.Event):
        """
        Check keyboard events and calls event handler for doing
        supporting actions.
        :param event: PyGame's object containing event
        """
        # TODO: Dima

    def gamepad_listener(self, event):
        """
        Check gamepad events and calls event handler for doing
        supporting actions.
        :param event:
        """
        # TODO: Dima

    def event_handler(self, eventName: str):
        """
        Does action from event name
        :param eventName: event name
        """
        if eventName == "quit":
            self.running = False
        # TODO: Dima

    def show(self):
        while self.running:
            self.clock.tick(Conf.Window.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.event_handler("quit")
                else:
                    self.keyboard_listener(event)
            self.sprites.draw(self.screen)
            pg.display.flip()
        pg.quit()
        # TODO: Dima
