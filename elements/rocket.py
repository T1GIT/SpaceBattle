import pygame as pg
from config import Configuration as Conf
import random as rd
from managers.image import Image as Img


class Rocket(pg.sprite.Sprite):
    """
    Class of the rocket's mobs.
    Flyes out from the rocket's nose.
    Destroys meteors
    """
    # TODO: Artem
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.raw_image = Img.get_rocket()
        w0, h0 = self.raw_image.get_size()
        scale = Conf.Rocket.SIZE / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.image = pg.transform.scale(self.raw_image, (w1, h1))

    def locate(self, x, y):
        """
        Shows sprite in the screen
        :param x: position
        :param y: position
        """
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):  # TODO доделать
        self.rect.x += 5
        if self.rect.left > Conf.Window.WIDTH:
            self.rect.right = 0