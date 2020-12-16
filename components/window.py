from ctypes import windll
from time import time_ns

import pygame as pg

from components.game import Game
from components.menu import Menu
from config import Configuration as Conf
from managers.event_listener.events import System as Sys, Keyboard as Kb, Gamepad as Gp, Device as Dvs, Event
from managers.event_listener.listener import EventListener
from managers.image import Image as Img
from managers.sound import Sound as Snd


class Window:
    """
    Class for show the main window.
    Initials the Game.
    Start event_listener
    """
    def __init__(self):
        # Initialisation
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(Conf.Window.TITLE)
        if Conf.Window.FULLSCREEN:
            user32 = windll.user32
            Conf.Window.WIDTH, Conf.Window.HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.screen = pg.display.set_mode((Conf.Window.WIDTH, Conf.Window.HEIGHT))
        # Environment
        self.clock = pg.time.Clock()
        self._esc_timer = 0
        self.running = False
        self.game_started = False
        # Sprites
        self.gp_all = pg.sprite.Group()
        # Components
        self.comp_game = Game(self)
        self.comp_menu = Menu(self)
        # Background
        bg = Img.get_background()
        w0, h0 = bg.get_size()
        scale = max((Conf.Window.WIDTH / w0, Conf.Window.HEIGHT / h0))
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.image = pg.transform.scale(bg, (w1, h1))

    def reset(self):
        """
        Reloads the game and opens the menu
        """
        self.comp_game.reset()
        self.gp_all.empty()

    def start(self):
        """
        Starts the game
        """
        self.game_started = True
        self.close_menu()
        if len(self.gp_all) > 0:
            self.reset()
        self.comp_game.start()
        self.mainloop()

    def open_menu(self):
        pg.event.set_grab(False)
        self.comp_menu.show()
        pg.mouse.set_visible(False)

    def close_menu(self):
        pg.mouse.set_visible(False)
        pg.event.set_grab(True)
        self.comp_menu.hide()
        Snd.bg_game()

    def event_handler(self, events: dict):
        """
        Does action from event name
        :param events: events dict
        """
        for event in events[Dvs.SYSTEM]:
            if event.get_type() == Sys.Events.QUIT:
                self.exit()
        for event in events[Dvs.KEYBOARD] | events[Dvs.GAMEPAD]:
            if ((event.get_data() == Kb.Keys.ESC
                    or (event.get_type() == Gp.Events.KEY and event.get_data() == Gp.Keys.START))
                    and (time_ns() - self._esc_timer) / 1e6 > Conf.Window.ESC_PERIOD):
                self._esc_timer = time_ns()
                self.open_menu()

    def exit(self):
        self.running = False
        self.comp_menu.hide()

    def show(self):
        self.running = True
        self.comp_menu.show()

    def mainloop(self):
        try:
            while self.running:
                self.loop(EventListener.get_events())
        except Exception as e:
            print(e)
        pg.quit()

    def loop(self, events: dict[int, set[Event]]):
        """
        Update all sprites and draw changes on the screen
        :param events
        """
        self.clock.tick(Conf.Rules.FPS)
        self.event_handler(events)
        self.comp_game.loop(events)
        self.screen.blit(self.image, self.image.get_rect())
        self.gp_all.update()
        self.gp_all.draw(self.screen)
        pg.display.flip()


