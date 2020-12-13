import pygame as pg
import ctypes

from event_listener.listener import EventListener
from event_listener.events import Keyboard as Kb, Gamepad as Gp, Mouse as Ms
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
        if Conf.Window.FULLSCREEN:
            user32 = ctypes.windll.user32
            width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
            self.screen = pg.display.set_mode((width, height), pg.FULLSCREEN)
        else:
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
        pg.mouse.set_visible(True)
        self.comp_game.reset()
        self.comp_menu.reset()
        self.sprites = pg.sprite.Group()

    def start(self):
        """
        Starts the game
        """
        pg.mouse.set_visible(False)
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
        self.event_listener.interrupt()
        self.running = False

    def show(self):
        self.event_listener.start()
        self.process()

    def process(self):

        self.player = Ship()
        self.player.locate(300, 300)
        self.sprites.add(self.player)
        pg.mouse.set_visible(False)

        try:
            while self.running:
                self.clock.tick(Conf.Window.FPS)
                if pg.event.peek(pg.QUIT): self.exit()

                x, y = 0, 0
                for event in self.event_listener.get_events():
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
                        self.player.rotate(*event.get_data())
                    elif event.get_type() == Gp.Events.RS:
                        self.player.rotate(*event.get_data())
                self.player.accelerate(x, y)

                self.comp_game.loop(self.event_listener.get_events())
                self.sprites.update()
                self.sprites.draw(self.screen)
                pg.display.flip()
                self.screen.fill((0, 0, 0))
        except Exception:
            self.exit()
        while self.event_listener.is_running():
            pass
        pg.quit()
