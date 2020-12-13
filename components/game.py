import random as rd

import pygame as pg

from components.overlay import Overlay
from config import Configuration as Conf
from elements.meteor import Meteor
from elements.rocket import Rocket
from event_listener.events import Event


def get_coords_for_meteor():
    """
    Get coordinates for meteor object
    :return: horizontally and vertically position
    """
    spawn_hor = Conf.Window.WIDTH // 2
    spawn_vert = Conf.Window.HEIGHT // 2
    while Conf.Window.WIDTH // 2 - 50 <= spawn_hor <= Conf.Window.WIDTH // 2 + 50:
        spawn_hor = rd.randint(10, Conf.Window.WIDTH)
    while Conf.Window.HEIGHT // 2 - 50 <= spawn_vert <= Conf.Window.HEIGHT // 2 + 50:
        spawn_vert = rd.randint(10, Conf.Window.HEIGHT)
    return spawn_hor, spawn_vert


class Game:
    def __init__(self, window):
        # Environment
        self.window = window
        self.counter_meteors = 0
        self.events = []
        # Initialisation
        self.sprites_meteors = pg.sprite.Group()
        self.sprites_rockets = pg.sprite.Group()
        # Components
        self.comp_overlay = Overlay(self)

    def reset(self):
        """
        Erases all mobs and objects
        """
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
        self.spawn_meteors()
        # TODO: Artem

    def event_handler(self, eventName: str):
        """
        Does action from event name
        :param eventName: event name
        """
        # Типа убийство метеора:
        self.counter_meteors -= 1
        # TODO: Artem

    def loop(self, events: [Event]):
        """
        Do all actions per one frame
        """
        self.spawn_meteors()

    def spawn_meteors(self):
        while self.counter_meteors < Conf.Meteor.QUANTITY:
            meteor = Meteor(self)
            meteor.locate(*get_coords_for_meteor())
            self.window.sprites.add(meteor)
            self.sprites_meteors.add(meteor)
            self.counter_meteors += 1
