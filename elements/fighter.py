from math import cos, sin, atan2, sqrt, degrees, radians
import random as rnd

import pygame as pg

from config import Configuration as Conf
from elements.rocket import Rocket
from elements.ship import Ship
from utils.image import Image as Img
from utils.sound import Sound as Snd


class Fighter(pg.sprite.Sprite):
    """
    Class of the enemy's mob
    Can shooting rockets
    Can by destroyed by meteors
    """
    _shoot_period = (Conf.System.FPS * Conf.Enemy.Fighter.SHOOT_PERIOD) // 1000

    def __init__(self, ship: Ship):
        super().__init__()
        self.ship = ship
        # Texture wearing
        raw_img = Img.get_fighter()
        w0, h0 = raw_img.get_size()
        scale = Conf.Ship.SIZE / max((w0, h0))
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.texture = pg.transform.scale(raw_img, (w1, h1))
        # Variables
        self.radius = min(self.texture.get_width(), self.texture.get_height()) / 2
        self.image = self.texture
        self.speed_x, self.speed_y = 0, 0
        self.angle = 90
        self.shoot_timer = 0

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
        d_x = rnd.choice((-1, 1))
        d_y = rnd.choice((-1, 1))
        if 0 + self.radius < self.rect.centerx + d_x < Conf.Window.WIDTH - self.radius:
            self.rect.x += d_x
        if 0 + self.radius < self.rect.centery + d_y < Conf.Window.HEIGHT - self.radius:
            self.rect.x += d_x
        if

    def rotate(self, x, y, smooth):
        """
        Rotates player's sprite in the direction of the vector.
        :param x: coordinate of the axel vector
        :param y: coordinate of the axel vector
        :param smooth: rotates not on the whole vector, but partially
        """
        d_deg = degrees(atan2(y, x)) - self.angle
        if d_deg > 180: d_deg -= 360
        elif d_deg < -180: d_deg += 360
        if (not smooth) or abs(d_deg) > self.accuracy * Conf.System.SCALE:
            self.angle += (d_deg / Conf.Ship.SMOOTH * Conf.System.SCALE) if smooth else d_deg
            self.image = pg.transform.rotate(
                self.texture_fire if self.with_fire else self.texture_normal, self.angle - 90)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.pos_x, self.pos_y = self.rect.x, self.rect.y
            if self.angle > 180: self.angle -= 360
            elif self.angle < -180: self.angle += 360

    def shoot(self):
        rocket = Rocket()
        ctr = self.rect.center
        rad = radians(-self.angle)
        x = ctr[0] + self.half_height * cos(rad)
        y = ctr[1] + self.half_height * sin(rad)
        rocket.locate(x, y, -self.angle)
        Snd.shoot()


    def _wear_fire(self, with_fire: bool):
        if with_fire != self.with_fire:
            self.with_fire = with_fire
            self.image = pg.transform.rotate(
                self.texture_fire if with_fire else self.texture_normal, self.angle - 90)
            self.rect = self.image.get_rect(center=self.rect.center)
            if with_fire: Snd.engine()

    @staticmethod
    def _resist(speed_x, speed_y):
        speed = sqrt(pow(speed_x, 2) + pow(speed_y, 2))
        rad = atan2(speed_y, speed_x)
        r = Conf.Ship.RESIST * pow(speed, 2)
        r_x = r * cos(rad)
        r_y = r * sin(rad)
        return r_x, r_y

    @staticmethod
    def _axel(x, y):
        if (x, y) == (0, 0): return 0, 0
        rad = atan2(y, x)
        f = Conf.Ship.POWER
        a_x = f * cos(rad) * pow(x, 2)
        a_y = f * sin(rad) * pow(y, 2)
        return a_x, a_y
