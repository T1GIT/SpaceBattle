from time import time_ns
import pygame as pg
from components.overlay import Overlay
from config import Configuration as Conf
from elements.meteor import Meteor
from event_listener.events import Event


class Game:
    def __init__(self, window):
        # Environment
        self.window = window
        self.counter_meteors = 0
        self.meteor_timer = 0
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
        if Conf.Meteor.BY_TIME:
            if time_ns() - self.meteor_timer > Conf.Meteor.PERIOD * 1e6:
                self.spawn_meteor()
                self.meteor_timer = time_ns()
        else:
            while self.counter_meteors < Conf.Meteor.QUANTITY:
                self.spawn_meteor()
                self.counter_meteors += 1

    def spawn_meteor(self):
        meteor = Meteor()
        if Conf.Meteor.ON_FIELD:
            meteor.locate(*Meteor.get_coords_for_meteor_on_field())
        else:
            meteor.locate(*Meteor.get_coords_for_meteor_out_field())
        self.window.sprites.add(meteor)
        self.sprites_meteors.add(meteor)