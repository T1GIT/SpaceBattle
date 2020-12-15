import pygame as pg

from components.overlay import Overlay
from config import Configuration as Conf
from elements.meteor import Meteor
from elements.ship import Ship
from event_listener.events import Keyboard as Kb, Gamepad as Gp, Mouse as Ms


class Game:
    """
    Class which initials the game.
    Spawns meteors.
    Catches events and redirect to the ship
    """
    rocket_period = (Conf.Rules.FPS * Conf.Rocket.PERIOD) // 1000
    meteor_period = (Conf.Rules.FPS * Conf.Meteor.PERIOD) // 1000

    def __init__(self, window):
        # Environment
        self.window = window
        self.counter_meteors = 0
        self.running = False
        # Sprites
        self.ship = None
        self.sprites_meteors = pg.sprite.Group()
        self.sprites_rockets = pg.sprite.Group()
        # Components
        self.comp_overlay = Overlay(self)
        # Timers
        self.meteor_timer = 0
        self.rocket_timer = 0

    def reset(self):
        """
        Erases all mobs and objects
        """
        self.ship.kill()
        for met in self.sprites_meteors:
            self.window.sprites.remove(met)
        for roc in self.sprites_rockets:
            self.window.sprites.remove(roc)
        self.sprites_rockets.empty()
        self.sprites_meteors.empty()

    def start(self):
        """
        Starts the game
        """
        self.ship = Ship()
        self.window.sprites.add(self.ship)
        self.ship.locate(Conf.Window.WIDTH // 2, Conf.Window.HEIGHT // 2)
        self.spawn_all_meteors()

    def event_handler(self, events: dict):
        """
        Does action from event name
        :param events
        """
        x, y = 0, 0
        for event_type, event_data in events.items():
            if event_type == Kb.Events.KEY:
                if event_data in (Kb.Keys.W, Kb.Keys.UP):       y += 1
                if event_data in (Kb.Keys.S, Kb.Keys.DOWN):     y -= 1
                if event_data in (Kb.Keys.A, Kb.Keys.LEFT):     x -= 1
                if event_data in (Kb.Keys.D, Kb.Keys.RIGHT):    x += 1
            elif event_type == Gp.Events.LS:    x, y = event_data
            if event_type == Ms.Events.MOVE:    self.ship.rotate(*event_data, True)
            elif event_type == Gp.Events.RS:    self.ship.rotate(*event_data, False)
            if ((event_type == Ms.Events.KEY and event_data == Ms.Keys.LEFT
                 or event_type == Gp.Events.KEY and event_data == Gp.Keys.RT)
                    and self.rocket_timer == 0):
                self.rocket_timer = self.rocket_period
                rocket = self.ship.shoot()
                self.window.sprites.add(rocket)
        self.ship.brake() if (x, y) == (0, 0) else self.ship.accelerate(x, y)

    def loop(self, events: dict):
        """
        Do all actions per one frame
        """
        # Events processing
        self.event_handler(events)
        # Spawning mobs
        self.spawn_all_meteors()
        # Decrementing timers
        self.meteor_timer = max(0, self.meteor_timer - 1)
        self.rocket_timer = max(0, self.rocket_timer - 1)

    def spawn_all_meteors(self):
        """
        Spawn all meteors by time or quantity configurations
        """
        if Conf.Meteor.BY_TIME:
            if self.meteor_timer == 0:
                self.meteor_timer = self.meteor_period
                self.spawn_meteor()
        else:
            while self.counter_meteors < Conf.Meteor.QUANTITY:
                self.spawn_meteor()
                self.counter_meteors += 1

    def spawn_meteor(self):
        """
        Spawn simple meteor on the field
        """
        meteor = Meteor()
        if Conf.Meteor.ON_FIELD:
            meteor.locate(*Meteor.SetMeteors().get_on_field())
        else:
            meteor.locate(*Meteor.SetMeteors().get_out_field())
        self.window.sprites.add(meteor)
        self.sprites_meteors.add(meteor)
