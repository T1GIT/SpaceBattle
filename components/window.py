import pygame as pg

from listeners.gamepad import GamepadListener
from listeners.keyboard import KeyboardListener
from managers.sound import Sound
from managers.image import Image
from components.game import Game
from components.menu import Menu
from config import Configuration as Conf


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
        # Listeners
        self.list_gamepad = GamepadListener()
        self.list_keyboard = KeyboardListener()

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

    def event_handler(self, eventName: str):
        """
        Does action from event name
        :param eventName: event name
        """
        if eventName == "quit":
            self.running = False
        # TODO: Dima

    def exit(self):
        self.list_keyboard.stop()
        self.list_gamepad.stop()
        pg.quit()

    def show(self):
        self.list_keyboard.start()
        # self.list_gamepad.start()
        self.process()

    def process(self):
        while self.running:
            self.clock.tick(Conf.Window.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.event_handler("quit")
            self.sprites.draw(self.screen)
            self.comp_game.loop()
            pg.display.flip()
        self.exit()
        # TODO: Dima
