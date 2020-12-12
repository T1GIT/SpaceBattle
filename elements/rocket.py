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
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.raw_image = Img.get_rocket()
        self.count_of_rocket = rd.randint(0, Conf.Images.ROCKET[1] - 1)
        w0, h0 = self.raw_image[self.count_of_rocket].get_size()
        scale = Conf.Rocket.SIZE / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.image = pg.transform.scale(self.raw_image[self.count_of_rocket], (w1, h1))
        self.rect = self.image.get_rect()
        self.rect.center = (Conf.Window.WIDTH // 2, Conf.Window.HEIGHT // 2)

    def update(self):  # TODO доделать
        self.rect.x += 5
        if self.rect.left > Conf.Window.WIDTH:
            self.rect.right = 0