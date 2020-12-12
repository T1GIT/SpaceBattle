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
        pg.display.set_caption(Conf.Window.TITLE)
        self.screen = pg.display.set_mode((Conf.Window.WIDTH, Conf.Window.HEIGHT))
        # Managers
        self.mng_sound = Sound()
        self.mng_image = Image()
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

    def event_handler(self, eventType):
        """
        Does action from event name
        :param eventType: event name
        """
        if eventType == pg.QUIT:
            self.running = False

    def exit(self):
        self.running = False
        self.list_keyboard.stop()
        self.list_gamepad.stop()
        pg.quit()

    def show(self):
        self.list_keyboard.start()
        # self.list_gamepad.start()  # TODO: Uncomment when gamepad_listener will be ready
        self.process()

    def process(self):
        while self.running:
            self.clock.tick(Conf.Window.FPS)
            for event in pg.event.get():
                self.event_handler(event.type)
            self.list_keyboard.erase()
            self.list_gamepad.erase()
            self.comp_game.loop()
            self.sprites.draw(self.screen)
            pg.display.flip()
            self.screen.fill((0, 0, 0))
        self.exit()
