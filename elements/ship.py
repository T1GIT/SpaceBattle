from math import cos, sin, atan2, sqrt, degrees, radians

import pygame as pg

from config import Configuration as Conf
from elements.rocket import Rocket
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
        self.half_width = self.texture.get_width() / 2
        self.half_height = self.texture.get_height() / 2
        self.image = self.texture.copy()
        self.x_speed, self.y_speed = 0, 0
        self.angle = 90
        self.accuracy = 50 / Conf.Ship.ACCURACY

    def locate(self, x, y):
        """
        Shows sprite in the screen
        :param x: position
        :param y: position
        """
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        """
        Updates ship coordinates.
        Adds the axis speed in the current time
        period to it's coordinates
        Called every frame.
        """
        d_x = round(self.x_speed)
        d_y = -round(self.y_speed)
        if 0 + self.half_width < self.rect.center[0] + d_x < Conf.Window.WIDTH - self.half_width:
            self.rect.x += d_x
        if 0 + self.half_width < self.rect.center[1] + d_y < Conf.Window.HEIGHT - self.half_width:
            self.rect.y += d_y

    def __resist(self):
        speed = sqrt(pow(self.x_speed, 2) + pow(self.y_speed, 2))
        rad = atan2(self.y_speed, self.x_speed)
        r = Conf.Ship.RESIST * pow(speed, 2)
        r_x = r * cos(rad)
        r_y = r * sin(rad)
        return r_x, r_y

    def __axel(self, x, y):
        if (x, y) == (0, 0): return 0, 0
        rad = atan2(y, x)
        f = Conf.Ship.POWER
        a_x = f * cos(rad) * pow(x, 2)
        a_y = f * sin(rad) * pow(y, 2)
        return a_x, a_y

    def accelerate(self, x, y):
        """
        Changes axis speed, from axel vector
        :param x: coordinate of the axel vector
        :param y: coordinate of the axel vector
        """
        # Adding resistance
        r = self.__resist()
        a = self.__axel(x, y)
        self.x_speed += (a[0] - r[0]) / Conf.Ship.WEIGHT
        self.y_speed += (a[1] - r[1]) / Conf.Ship.WEIGHT

    def brake(self):
        r = self.__resist()
        self.x_speed -= r[0] / Conf.Ship.WEIGHT
        self.y_speed -= r[1] / Conf.Ship.WEIGHT

    def rotate(self, x, y, smooth):
        """
        Rotates player's sprite in the direction of the vector.
        :param x: coordinate of the axel vector
        :param y: coordinate of the axel vector
        :param smooth: rotates not on the whole vector, but
            partially
        """
        d_deg = degrees(atan2(y, x)) - self.angle
        if d_deg > 180: d_deg -= 360
        elif d_deg < -180: d_deg += 360
        if (not smooth) or abs(d_deg) > self.accuracy:
            self.angle += (d_deg / Conf.Ship.SMOOTH) if smooth else d_deg
            self.image = pg.transform.rotate(self.texture, self.angle - 90)
            self.rect = self.image.get_rect(center=self.rect.center)
            if self.angle > 180: self.angle -= 360
            elif self.angle < -180: self.angle += 360

    def shoot(self):
        rocket = Rocket()
        ctr = self.rect.center
        rad = radians(-self.angle)
        x = ctr[0] + self.half_height * cos(rad)
        y = ctr[1] + self.half_height * sin(rad)
        rocket.locate(x, y, -self.angle)
        return rocket
