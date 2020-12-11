import pygame as pg

from components.game import Game
from managers.config import Configuration as Conf


class Overlay:
    def __init__(self, game: Game):
        self.game = game
        pass

    def reset(self):
        """
        Zero out all variables
        """
        # TODO: Damir

    def up_score(self):
        """
        Raises score in the overlay
        """
        # May request delta in func parameter, or write it into Conf.Overlay
        # TODO: Damir

    def down_life(self):
        """
        Subtracts one life
        """
        # TODO: Damir

    def is_alive(self) -> bool:
        """
        Checks if is it has lifes
        :return True if it has lifes
        """
        # TODO: Damir
