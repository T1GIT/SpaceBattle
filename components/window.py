import pygame as pg

from managers.listener import EventListener
from managers.sound import Sound
from managers.image import Image
from components.game import Game
from components.menu import Menu
from config import Configuration as Conf


from elements.ship import Ship


class Window:
    def __init__(self):
        # Initialisation
        pg.init()
        pg.display.set_caption(Conf.Window.TITLE)
        self.screen = pg.display.set_mode((Conf.Window.WIDTH, Conf.Window.HEIGHT))
        # Environment
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        self.running = True
        # Managers
        self.mng_sound = Sound()
        self.mng_image = Image()
        # Components
        self.comp_game = Game(self)
        self.comp_menu = Menu(self)
        # Listeners
        self.event_listener = EventListener()

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
        self.event_listener.stop()
        self.running = False

    def show(self):
        self.event_listener.start()
        self.process()

    def process(self):

        self.player = Ship()
        self.player.locate(20, 20)
        self.sprites.add(self.player)

        while self.running:
            self.clock.tick(Conf.Window.FPS)
            if pg.event.peek(pg.QUIT): self.exit()
            self.comp_game.loop(self.event_listener.pop_events())
            self.sprites.update()
            self.sprites.draw(self.screen)
            pg.display.flip()
            self.screen.fill((0, 0, 0))
        while self.event_listener.is_running():
            pass
        self.exit()
