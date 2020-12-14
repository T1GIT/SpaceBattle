import pygame as pg
from ctypes import windll
from time import time_ns

from event_listener.listener import EventListener
from event_listener.events import Keyboard as Kb, Gamepad as Gp, Mouse as Ms, Event
from managers.sound import Sound
from managers.image import Image
from components.game import Game
from components.menu import Menu
from config import Configuration as Conf
from managers.image import Image as Img


from elements.ship import Ship


class Window:
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
        self.running = True
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



        self.rocket_timer = 0

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
        pg.mouse.set_visible(False)
        self.comp_game.start()
        self.comp_menu.hide()

    def menu(self):
        self.comp_game.reset()
        self.comp_menu.show()

    def event_handler(self, events: [Event]):
        """
        Does action from event name
        :param events: list of the events
        """
        for event in events:
            if event.type == pg.QUIT:
                self.exit()

    def exit(self):
        self.running = False
        self.event_listener.interrupt()
        self.comp_menu.exit()

    def show(self):
        self.running = True
        # self.comp_menu.show()
        if self.running:
            self.event_listener.start()
            self.mainloop()

    def mainloop(self):
        pg.mouse.set_visible(False)
        pg.event.set_grab(True)

        self.ship = Ship()  # TODO: Move into Game.event_handler after testing finish
        self.ship.locate(Conf.Window.WIDTH // 2, Conf.Window.HEIGHT // 2)
        self.sprites.add(self.ship)

        try:
            while self.running:
                if pg.event.peek(pg.QUIT):
                    self.exit()
                else:
                    self.loop(self.event_listener.pop_events())
        except Exception as e:
            print(e)
            self.exit()
        pg.quit()

    def loop(self, events: [Event]):
        self.screen.blit(self.image, self.image.get_rect())
        self.sprites.draw(self.screen)
        self.comp_game.loop(self.event_listener.pop_events())
        self.sprites.update()
        pg.display.flip()
        self.clock.tick(Conf.Rules.FPS)

        x, y = 0, 0  # TODO: Move into Game.event_handler after testing finish
        for event in events:
            if event.get_type() == Kb.Events.KEY:
                if event.get_data() in (Kb.Keys.W, Kb.Keys.UP):
                    y += 1
                if event.get_data() in (Kb.Keys.S, Kb.Keys.DOWN):
                    y -= 1
                if event.get_data() in (Kb.Keys.A, Kb.Keys.LEFT):
                    x -= 1
                if event.get_data() in (Kb.Keys.D, Kb.Keys.RIGHT):
                    x += 1
            elif event.get_type() == Gp.Events.LS:
                x += event.get_data()[0]
                y += event.get_data()[1]
            elif event.get_type() == Ms.Events.MOVE:
                self.ship.rotate(*event.get_data(), True)
            elif event.get_type() == Gp.Events.RS:
                self.ship.rotate(*event.get_data(), False)
            elif (event.get_type() == Ms.Events.KEY and event.get_data() == Ms.Keys.LEFT
                  or event.get_type() == Gp.Events.KEY and event.get_data() == Gp.Keys.RT):
                if (time_ns() - self.rocket_timer) / 1e6 > Conf.Rocket.PERIOD:
                    self.rocket_timer = time_ns()
                    rocket = self.ship.shoot()
                    self.sprites.add(rocket)
        if (x, y) == (0, 0):
            self.ship.brake()
        else:
            self.ship.accelerate(x, y)
