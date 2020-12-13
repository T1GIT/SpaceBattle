import pygame as pg
from math import cos, sin, tan, acos, asin, atan, sqrt, pi

from config import Configuration as Conf
from managers.image import Image as Img


class Ship(pg.sprite.Sprite):
    """
    Class of the player's mob
    Can shooting rockets
    Can by destroyed by meteors
    """
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        raw_image = Img.get_ship()
        w0, h0 = raw_image.get_size()
        scale = Conf.Ship.SIZE / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.image = pg.transform.scale(raw_image, (w1, h1))
        self._max_speed = sqrt(Conf.Ship.POWER / Conf.Ship.RESIST)
        self.x_speed = 0
        self.y_speed = 0

    def locate(self, x, y):
        """
        Shows sprite in the screen
        :param x: position
        :param y: position
        """
        self.rect = self.image.get_rect(
            center=(x, y))

    def update(self):
        self.rect.x += round(self.x_speed)
        self.rect.y -= round(self.y_speed)

    def accelerate(self, x, y):
        # Adding resistance
        speed = sqrt(pow(self.x_speed, 2) + pow(self.y_speed, 2))
        a_x, a_y = 0, 0
        if speed != 0:
            rad = self.get_angle(self.x_speed, self.y_speed)
            r = Conf.Ship.RESIST * pow(speed, 2)
            a_x -= r * cos(rad)
            a_y -= r * sin(rad)
        # Adding accel
        gas = min(1.0, sqrt(pow(x, 2) + pow(y, 2)))
        if x != 0 or y != 0:
            rad = self.get_angle(x, y)
            f = Conf.Ship.POWER
            a_x += f * cos(rad)
            a_y += f * sin(rad)
        self.x_speed += a_x / Conf.Ship.WEIGHT
        self.y_speed += a_y / Conf.Ship.WEIGHT

    @staticmethod
    def get_angle(x, y):
        if x == 0:
            if y > 0: rad = pi / 2
            else: rad = pi * 3 / 2
        elif y == 0:
            rad = 0
        else:
            rad = atan(y / x)
        if x < 0: rad += pi
        return rad

