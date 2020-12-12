import pygame as pg
from config import Configuration as Conf


class Rocket(pg.sprite.Sprite):
    """
    Class of the rocket's mobs.
    Flyes out from the rocket's nose.
    Destroys meteors
    """
    # TODO: Artem
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((Conf.Rocket.SIZE, Conf.Rocket.SIZE))
        self.image.fill("blue")
        self.rect = self.image.get_rect()

    def update(self):
        pass