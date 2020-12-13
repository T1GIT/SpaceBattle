import pygame as pg
from config import Configuration as Conf
from managers.image import Image as Img
from math import cos, sin, radians, sqrt


class Rocket(pg.sprite.Sprite):
    """
    Class of the rocket's mobs.
    Flies out from the rocket's nose.
    Destroys meteors
    """
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        raw_image = Img.get_rocket()
        w0, h0 = raw_image.get_size()
        scale = Conf.Rocket.SIZE / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.texture = pg.transform.scale(raw_image, (w1, h1))
        self.image = self.texture.copy()
        self.x, self.y = 0, 0
        self.a_x, self.a_y = 0, 0
        self.angle = 0

    def locate(self, x, y, deg):
        """
        Shows sprite in the screen
        :param x: position
        :param y: position
        :param deg: angle of rotation
        """
        self.x, self.y = x, y
        self.angle = deg
        rad = radians(self.angle)
        self.a_x = round(Conf.Rocket.SIZE * Conf.Rocket.SPEED * cos(rad))
        self.a_y = round(Conf.Rocket.SIZE * Conf.Rocket.SPEED * sin(rad))
        self.image = pg.transform.rotate(self.texture, -self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        if Conf.Rocket.INFINITY:
            if 0 < self.rect.x < Conf.Window.WIDTH and 0 < self.rect.y < Conf.Window.HEIGHT:
                self.rect.x += self.a_x
                self.rect.y += self.a_y
            else:
                self.kill()
        else:
            if sqrt(pow(self.rect.x - self.x, 2) + pow(self.rect.y - self.y, 2)) <= Conf.Rocket.MAX_DISTANCE:
                self.rect.x += self.a_x
                self.rect.y += self.a_y
            else:
                self.kill()
