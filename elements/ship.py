import pygame as pg

from config import Configuration as Conf
from managers.image import Image as Img


class Ship(pg.sprite.Sprite):
    """
    Class of the player's mob
    Can shooting rockets
    Can by destroyed by meteors
    """
    # TODO: Dima
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        raw_image = Img.SHIP
        scale = Conf.
        self.image = pg.

    def locate(self, x, y):
        self.rect = self.image.get_rect(
            center=(x, y))

    def update(self):
        pass
