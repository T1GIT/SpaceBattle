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
        raw_image = Img.get_ship()
        width, height = raw_image.get_size()
        scale = Conf.Ship.SIZE / height
        self.image = pg.transform.scale(raw_image, (width * scale, height * scale))

    def locate(self, x, y):
        """
        Shows sprite in the screen
        :param x: position
        :param y: position
        """
        self.rect = self.image.get_rect(
            center=(x, y))

    def update(self):
        pass
