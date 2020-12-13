from math import cos, sin, atan2, sqrt, degrees

import pygame as pg

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
        self.texture = pg.transform.scale(raw_image, (w1, h1))
        self.image = self.texture.copy()
        self.x_speed = 0
        self.y_speed = 0
        self.angle = 0
        self.accuracy = 50 / Conf.Ship.ACCURACY

    def locate(self, x, y):
        """
        Shows sprite in the screen
        :param x: position
        :param y: position
        """
        self.rect = self.image.get_rect(
            center=(x, y))

    def update(self):
        """
        Updates ship coordinates.
        Adds the axis speed in the current time
        period to it's coordinates
        Called every frame.
        """
        self.rect.x += round(self.x_speed)
        self.rect.y -= round(self.y_speed)

    def accelerate(self, x, y):
        """
        Changes axis speed, from axel vector
        :param x: coordinate of the axel vector
        :param y: coordinate of the axel vector
        """
        # Adding resistance
        speed = sqrt(pow(self.x_speed, 2) + pow(self.y_speed, 2))
        a_x, a_y = 0, 0
        if speed != 0:
            rad = atan2(self.y_speed, self.x_speed)
            r = Conf.Ship.RESIST * pow(speed, 2)
            a_x -= r * cos(rad)
            a_y -= r * sin(rad)
        # Adding accel
        if x != 0 or y != 0:
            rad = atan2(y, x)
            f = Conf.Ship.POWER
            a_x += f * cos(rad) * pow(x, 2)
            a_y += f * sin(rad) * pow(y, 2)
        self.x_speed += a_x / Conf.Ship.WEIGHT
        self.y_speed += a_y / Conf.Ship.WEIGHT

    def rotate(self, x, y, smooth):
        """
        Rotates player's sprite in the direction of the vector.
        :param x: coordinate of the axel vector
        :param y: coordinate of the axel vector
        :param smooth: rotates not on the whole vector, but
            partially
        """
        d_deg = degrees(atan2(y, x)) - self.angle
        if d_deg > 180:
            d_deg -= 360
        elif d_deg < -180:
            d_deg += 360
        if (not smooth) or abs(d_deg) > self.accuracy:
            self.angle += (d_deg / Conf.Ship.SMOOTH) if smooth else d_deg
            self.image = pg.transform.rotate(self.texture, self.angle - 90)
            self.rect = self.image.get_rect(center=self.rect.center)
            if self.angle > 180:
                self.angle -= 360
            elif self.angle < -180:
                self.angle += 360
