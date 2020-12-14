import pygame as pg
from config import Configuration as Conf
import random as rd
from managers.image import Image as Img


class Meteor(pg.sprite.Sprite):
    """
    Class of the meteor's mobs
    Can destroy ship
    Can be destroyed by rockets
    """
    def __init__(self):
        # Settings
        self.speed_x = rd.uniform(-Conf.Meteor.MAX_SPEED, Conf.Meteor.MAX_SPEED)
        self.speed_y = rd.uniform(-Conf.Meteor.MAX_SPEED, Conf.Meteor.MAX_SPEED)
        self.angle_speed = rd.uniform(-Conf.Meteor.MAX_ROTATE_SPEED, Conf.Meteor.MAX_ROTATE_SPEED) * Conf.Rules.SCALE
        self.pos_x, self.pos_y = 0, 0
        # Init sprite
        pg.sprite.Sprite.__init__(self)
        raw_image = Img.get_meteors()
        self.count_of_meteor = rd.randint(0, len(raw_image) - 1)
        w0, h0 = raw_image[self.count_of_meteor].get_size()
        scale = rd.randint(Conf.Meteor.MIN_SIZE, Conf.Meteor.MAX_SIZE) / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.texture = pg.transform.scale(raw_image[self.count_of_meteor], (w1, h1))
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
        self.pos_x += self.speed_x * Conf.Rules.SCALE
        self.pos_y += self.speed_y * Conf.Rules.SCALE
        self.rect.x, self.rect.y = self.pos_x, self.pos_y
        if self.rect.left > Conf.Window.WIDTH + Conf.Meteor.MAX_SIZE:
            self.rect.right = 0
            self.pos_x = self.rect.x
        elif self.rect.right < 0 - Conf.Meteor.MAX_SIZE:
            self.rect.left = Conf.Window.WIDTH
            self.pos_x = self.rect.x
        if self.rect.top > Conf.Window.HEIGHT + Conf.Meteor.MAX_SIZE:
            self.rect.bottom = 0
            self.pos_y = self.rect.y
        elif self.rect.bottom < 0 - Conf.Meteor.MAX_SIZE:
            self.rect.top = Conf.Window.HEIGHT
        self.pos_x, self.pos_y = self.rect.x, self.rect.y
        if Conf.Meteor.ROTATING:
            self.rotate()

    class SetMeteors:
        @staticmethod
        def get_on_field():
            """
            Get coordinates on field for meteor object
            :return: horizontally and vertically position
            """
            x = rd.uniform(0 + 50, Conf.Window.WIDTH - 50)
            y = rd.uniform(0 + 50, Conf.Window.HEIGHT - 50)
            return x, y

        @staticmethod
        def get_out_field():
            """
            Get coordinates out of field for meteor object
            :return: horizontally and vertically position
            """
            if rd.random() > 0.5:
                x = rd.choice(
                    (rd.uniform(-Conf.Meteor.MAX_SIZE, 0),
                     rd.uniform(Conf.Window.WIDTH, Conf.Window.WIDTH + Conf.Meteor.MAX_SIZE)))
                y = rd.uniform(-Conf.Meteor.MAX_SIZE, Conf.Window.HEIGHT + Conf.Meteor.MAX_SIZE)
            else:
                x = rd.uniform(-Conf.Meteor.MAX_SIZE, Conf.Window.WIDTH + Conf.Meteor.MAX_SIZE)
                y = rd.choice(
                    (rd.uniform(-Conf.Meteor.MAX_SIZE, 0),
                     rd.uniform(Conf.Window.HEIGHT, Conf.Window.HEIGHT + Conf.Meteor.MAX_SIZE)))
            return x, y
