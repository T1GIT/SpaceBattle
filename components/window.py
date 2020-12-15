from ctypes import windll

import pygame as pg

from components.game import Game
from components.menu import Menu
from config import Configuration as Conf
from event_listener.listener import EventListener
from managers.image import Image
from managers.image import Image as Img
from managers.sound import Sound


class Window:
    """
    Class for show the main window.
    Initials the Game.
    Start event_listener
    """
    def __init__(self):
        # Initialisation
        pg.init()
        pg.display.set_caption(Conf.Window.TITLE)
        if Conf.Window.FULLSCREEN:
            user32 = windll.user32
            Conf.Window.WIDTH, Conf.Window.HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.screen = pg.display.set_mode((Conf.Window.WIDTH, Conf.Window.HEIGHT))
        # Environment
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        self.running = False
        # Managers
        self.mng_sound = Sound()
        self.mng_image = Image()
        # Components
        self.comp_game = Game(self)
        self.comp_menu = Menu(self)
        # Listeners
        self.event_listener = EventListener()
        # Background
        bg = Img.get_static_bg()
        w0, h0 = bg.get_size()
        scale = max((Conf.Window.WIDTH / w0, Conf.Window.HEIGHT / h0))
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.image = pg.transform.scale(bg, (w1, h1))

    def reset(self):
        """
        Reloads the game and opens the menu
        """
        pg.mouse.set_visible(True)
        self.comp_game.reset()
        self.comp_menu.show()
        self.sprites = pg.sprite.Group()

    def start(self):
        """
        Starts the game
        """
        # pg.mouse.set_visible(False)
        # pg.event.set_grab(True)
        self.comp_menu.hide()
        self.comp_game.start()
        self.mainloop()

    def menu(self):
        """
        Opens the menu
        """
        pg.mouse.set_visible(True)
        pg.event.set_grab(False)
        self.comp_menu.show()

    def event_handler(self, events: dict):
        """
        Does action from event name
        :param events: events dict
        """
        if pg.QUIT in events:
            self.exit()

    def exit(self):
        """
        Close menu window
        """
        self.running = False
        self.event_listener.interrupt()
        self.comp_menu.hide()

    def show(self):
        """
        Opens the window
        """
        self.running = True
        self.event_listener.start()
        self.comp_menu.show()

    def mainloop(self):
        """
        Main method of the class
        Start event_handler
        """
        try:
            while self.running:
                self.loop(self.event_listener.get_events())
                self.event_listener.erase()
        except Exception as e:
            print(e)
            self.exit()
        pg.quit()

    def loop(self, events: dict):
        """
        Update all sprites and draw changes on the screen
        :param events
        """
        self.event_handler(events)
        self.screen.blit(self.image, self.image.get_rect())
        self.comp_game.loop(events)
        self.sprites.update()
        self.sprites.draw(self.screen)
        pg.display.flip()
        self.clock.tick(Conf.Rules.FPS)


