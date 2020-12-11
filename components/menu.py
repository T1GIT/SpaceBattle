import pygame as pg

from components.window import Window
from managers.config import Configuration as Conf


class Menu:
    def __init__(self, window: Window):
        # Environment
        self.window = window
        # Initialisation
        # TODO: Damir

    def reset(self):
        """
        Shows menu
        """
        # TODO: Damir

    def start(self):
        """
        Hiding menu and runs the game
        """
        self.window.start()
        # TODO: Damir
