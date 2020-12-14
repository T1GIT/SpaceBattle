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
        # Settings
        self.size = Conf.Rocket.SIZE
        self.speed = Conf.Rocket.SPEED
        self.max_dist = Conf.Rocket.MAX_DISTANCE
        self.angle = 0
        self.start_x, self.start_y = 0, 0
        self.a_x, self.a_y = 0, 0
        # Init sprite
        pg.sprite.Sprite.__init__(self)
        raw_image = Img.get_rocket()
        w0, h0 = raw_image.get_size()
        scale = self.size / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.texture = pg.transform.scale(raw_image, (w1, h1))
        self.image = self.texture

    def locate(self, x, y, deg):
        """
        Shows sprite in the screen
        :param x: position
        :param y: position
        :param deg: angle of rotation
        """
        self.angle = deg
        rad = radians(self.angle)
        self.start_x, self.start_y = x, y
        self.a_x = round(self.speed * cos(rad))
        self.a_y = round(self.speed * sin(rad))
        self.image = pg.transform.rotate(self.texture, -self.angle)
        self.rect = self.image.get_rect(center=(self.start_x, self.start_y))

    def update(self):
        ctr = self.rect.center
        if Conf.Rocket.UNLIMITED:
            if 0 < ctr[0] < Conf.Window.WIDTH and 0 < ctr[1] < Conf.Window.HEIGHT:
                self.rect.x += self.a_x
                self.rect.y += self.a_y
            else:
                self.kill()
        else:
            if sqrt(pow(ctr[0] - self.start_x, 2) + pow(ctr[1] - self.start_y, 2)) <= self.max_dist:
                self.rect.x += self.a_x
                self.rect.y += self.a_y
            else:
                self.kill()
