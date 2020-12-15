import pygame as pg

from components.overlay import Overlay
from config import Configuration as Conf
from elements.meteor import Meteor
from elements.ship import Ship
from managers.event_listener.events import Keyboard as Kb, Gamepad as Gp, Mouse as Ms, Event
from managers.sound import Sound as Snd


def is_correct_mask(sprite1, sprite2):
    mask1 = pg.mask.from_surface(sprite1.image)
    mask2 = pg.mask.from_surface(sprite2.image)
    offset = (int(sprite2.rect.x - sprite1.rect.x), int(sprite2.rect.y - sprite1.rect.y))
    if mask1.overlap_area(mask2, offset) > 0:
        return False
    return True


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
        self.running = False
        self.ship.kill()
        self.sprites_rockets.empty()
        self.sprites_meteors.empty()
        self.counter_meteors = 0
        self.meteor_timer = 0
        self.rocket_timer = 0
        self.comp_overlay.reset()

    def start(self):
        """
        Starts the game
        """
        self.ship = Ship()
        self.window.sprites.add(self.ship)
        self.ship.locate(Conf.Window.WIDTH // 2, Conf.Window.HEIGHT // 2)
        self.spawn_all_meteors()
        Snd.bg_game()

    def event_handler(self, events: [Event]):
        """
        Does action from event name
        :param events
        """
        x, y = 0, 0
        shoot = False
        for event in events["mouse"]:
            if event.get_type() == Ms.Events.MOVE:
                self.ship.rotate(*event.get_data(), True)
            if event.get_type() == Ms.Events.KEY and event.get_data() == Ms.Keys.LEFT:
                shoot = True
        for event in events["keyboard"]:
            if event.get_data() in (Kb.Keys.W, Kb.Keys.UP):       y += 1
            if event.get_data() in (Kb.Keys.A, Kb.Keys.LEFT):     x -= 1
            if event.get_data() in (Kb.Keys.S, Kb.Keys.DOWN):     y -= 1
            if event.get_data() in (Kb.Keys.D, Kb.Keys.RIGHT):    x += 1
        for event in events["gamepad"]:
            if event.get_type() == Gp.Events.LS:    x, y = event.get_data()
            if event.get_type() == Gp.Events.RS:    self.ship.rotate(*event.get_data(), False)
            if event.get_type() == Gp.Events.KEY and event.get_data() == Gp.Keys.RT:
                shoot = True
        # Shooting
        if shoot and self.rocket_timer == 0:
            self.rocket_timer = self.rocket_period
            rocket = self.ship.shoot()
            self.window.sprites.add(rocket)
            self.sprites_rockets.add(rocket)
        # Moving
        if (x, y) == (0, 0):
            self.ship.brake()
        else:
            self.ship.accelerate(x, y)

    def loop(self, events: dict):
        """
        Do all actions per one frame
        """
        # Events processing
        self.event_handler(events)
        # Collide sprites
        self.col_met_ship()
        if self.sprites_rockets.sprites():
            self.col_met_roc()
        # Spawning mobs
        self.spawn_all_meteors()
        # Decrementing timers
        self.meteor_timer = max(0, self.meteor_timer - 1)
        self.rocket_timer = max(0, self.rocket_timer - 1)

    def col_met_ship(self):
        for met in self.sprites_meteors.sprites():
            if met.rect.right > self.ship.rect.left and met.rect.left < self.ship.rect.right and \
                    met.rect.bottom > self.ship.rect.top and met.rect.top < self.ship.rect.bottom and \
                    not is_correct_mask(self.ship, met):
                self.ship.kill()
                met.kill()

    def col_met_roc(self):
        for roc in self.sprites_rockets.sprites():
            for met in self.sprites_meteors.sprites():
                if met.rect.right > roc.rect.left and met.rect.left < roc.rect.right and \
                        met.rect.bottom > roc.rect.top and met.rect.top < roc.rect.bottom and \
                        not is_correct_mask(met, roc):
                    roc.kill()
                    met.kill()

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
