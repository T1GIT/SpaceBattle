import random as rnd

import pygame as pg

from config import Configuration as Conf
from managers.image import Image as Img


class Meteor(pg.sprite.Sprite):
    """
    Class of the meteor's mobs
    Can destroy ship
    Can be destroyed by rockets
    """
    def __init__(self):
        # Settings
        self.speed_x = rnd.uniform(-Conf.Meteor.MAX_SPEED, Conf.Meteor.MAX_SPEED) * Conf.Rules.SCALE
        self.speed_y = rnd.uniform(-Conf.Meteor.MAX_SPEED, Conf.Meteor.MAX_SPEED) * Conf.Rules.SCALE
        self.angle_speed = rnd.uniform(-Conf.Meteor.MAX_ROTATE_SPEED, Conf.Meteor.MAX_ROTATE_SPEED) * Conf.Rules.SCALE
        self.pos_x, self.pos_y = 0, 0
        # Initialising sprite
        pg.sprite.Sprite.__init__(self)
        raw_image = Img.get_meteors()
        self.amount = rnd.randint(0, len(raw_image) - 1)
        w0, h0 = raw_image[self.amount].get_size()
        scale = rnd.randint(Conf.Meteor.MIN_SIZE, Conf.Meteor.MAX_SIZE) / max(w0, h0)
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.texture = pg.transform.scale(raw_image[self.amount], (w1, h1))
        self.image = self.texture
        self.angle = 0

    def rotate(self):
        """
        Rotate the figure
        """
        x_offset = self.pos_x - self.rect.x
        y_offset = self.pos_y - self.rect.y
        self.angle = (self.angle + self.angle_speed) % 360
        self.image = pg.transform.rotate(self.texture, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.pos_x = self.rect.x + x_offset
        self.pos_y = self.rect.y + y_offset

    def locate(self, x, y):
        """
        Shows sprite in the screen
        :param x: position of the end
        :param y: position of the end
        """
        self.rect = self.image.get_rect(center=(x, y))
        self.pos_x, self.pos_y = self.rect.x, self.rect.y

    def update(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        self.rect.x, self.rect.y = self.pos_x, self.pos_y
        max_size = Conf.Meteor.MAX_SIZE
        width = Conf.Window.WIDTH
        height = Conf.Window.HEIGHT
        if self.rect.left < -max_size:
            self.rect.left = width
            self.pos_x = self.rect.x
        elif self.rect.right > width + max_size:
            self.rect.right = 0
            self.pos_x = self.rect.x
        if self.rect.top < -max_size:
            self.rect.top = height
            self.pos_y = self.rect.y
        elif self.rect.bottom > height + max_size:
            self.rect.bottom = 0
            self.pos_y = self.rect.y
        if Conf.Meteor.ROTATING:
            self.rotate()

    class SetMeteors:
        @staticmethod
        def get_on_field():
            """
            Get coordinates on field for meteor object
            :return: horizontally and vertically position
            """
            x = rnd.uniform(0, Conf.Window.WIDTH)
            y = rnd.uniform(0, Conf.Window.HEIGHT)
            return x, y

        @staticmethod
        def get_out_field():
            """
            Get coordinates out of field for meteor object
            :return: horizontally and vertically position
            """
            if rnd.random() > 0.5:
                x = rnd.choice((-Conf.Meteor.MAX_SIZE / 2, Conf.Window.WIDTH + Conf.Meteor.MAX_SIZE / 2))
                y = rnd.uniform(-Conf.Meteor.MAX_SIZE / 2, Conf.Window.HEIGHT + Conf.Meteor.MAX_SIZE / 2)
            else:
                x = rnd.uniform(-Conf.Meteor.MAX_SIZE / 2, Conf.Window.WIDTH + Conf.Meteor.MAX_SIZE / 2)
                y = rnd.choice((-Conf.Meteor.MAX_SIZE / 2, Conf.Window.HEIGHT + Conf.Meteor.MAX_SIZE / 2))
            return x, y
