import pygame as pg
from math import cos, sin, tan, acos, asin, atan2, sqrt, pi, degrees, atan

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
        self._max_speed = sqrt(Conf.Ship.POWER / Conf.Ship.RESIST)
        self.x_speed = 0
        self.y_speed = 0
        self.angle = 0

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

    def rotate(self, x, y):
        move = atan2(y, x)
        self.angle = degrees(move)

        self.image = pg.transform.rotate(self.texture, self.angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)
        # if abs(d_deg) > 100 / Conf.Ship.ACCURACY:
        #     self.angle += d_deg / Conf.Ship.SMOOTH
        #     self.angle = (self.angle + 180) % 360 - 180
        #     self.image = pg.transform.rotate(self.texture, self.angle - 90)
        #     self.rect = self.image.get_rect(center=self.rect.center)

        # move = degrees(self.__get_angle(x, y))
        # if abs(move - self.angle) > 180 and abs(self.angle) > 90 and abs(move) > 90:
        #     d_deg = (360 - abs(self.angle - move)) * -1 if self.angle < move else 1
        #     print(1)
        # else:
        #     d_deg = move - self.angle

        # print(move, d_deg, self.angle)
        # if abs(d_deg) > 100 / Conf.Ship.ACCURACY:
        #     self.angle += d_deg / Conf.Ship.SMOOTH
        #     self.angle = (self.angle + 180) % 360 - 180
        #     self.image = pg.transform.rotate(self.texture, self.angle - 90)
        #     self.rect = self.image.get_rect(center=self.rect.center)

