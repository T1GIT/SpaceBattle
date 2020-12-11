import pygame as pg

from components.overlay import Overlay
from components.window import Window
from managers.config import Configuration as Conf


class Game:
    def __init__(self, window: Window):
        # Environment
        self.window = window
        # Initialisation

        # Components
        self.comp_overlay = Overlay(self)
        # TODO: Artem

    def reset(self):
        """
        Erases all mobs and objects
        """
        # TODO: Artem

    def start(self):
        """
        Starts the game
        """
        # TODO: Artem

    def loop(self):
        """
        Do all actions per one frame
        """
        # TODO: Artem
