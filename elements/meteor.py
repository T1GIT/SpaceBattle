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
        self.max_speed = Conf.Meteor.MAX_SPEED
        self.min_speed = Conf.Meteor.MIN_SPEED
        self.min_size = Conf.Meteor.MIN_SIZE
        self.max_size = Conf.Meteor.MAX_SIZE
        self.speed_x = rd.choice((-1, 1)) * rd.uniform(self.min_speed, self.max_speed)
        self.speed_y = rd.uniform(-self.max_speed, self.max_speed)
        self.angle = 0
        self.angle_speed = rd.uniform(-Conf.Meteor.MAX_ROTATE_SPEED, Conf.Meteor.MAX_ROTATE_SPEED) * Conf.Rules.SCALE
        self.pos_x, self.pos_y = 0, 0
        # Init sprite
        pg.sprite.Sprite.__init__(self)
        raw_image = Img.get_meteors()
        self.count_of_meteor = rd.randint(0, len(raw_image) - 1)
        w0, h0 = raw_image[self.count_of_meteor].get_size()
        scale = rd.randint(self.min_size, self.max_size) / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.texture = pg.transform.scale(raw_image[self.count_of_meteor], (w1, h1))
        self.image = self.texture

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
        if self.rect.left > Conf.Window.WIDTH + self.max_size:
            self.rect.right = 0
            self.pos_x = self.rect.x
        elif self.rect.right < 0 - self.max_size:
            self.rect.left = Conf.Window.WIDTH
            self.pos_x = self.rect.x
        if self.rect.top > Conf.Window.HEIGHT + self.max_size:
            self.rect.bottom = 0
            self.pos_y = self.rect.y
        elif self.rect.bottom < 0 - self.max_size:
            self.rect.top = Conf.Window.HEIGHT
            self.pos_y = self.rect.y
        if Conf.Meteor.ROTATING:
            self.rotate()

    class Set_Meteors:
        def __init__(self):
            self.meteor_size = Conf.Meteor.MAX_SIZE
            self.where = rd.choice((False, True))
            self.x, self.y = 0, 0

        def get_on_field(self):
            """
            Get coordinates on field for meteor object
            :return: horizontally and vertically position
            """
            self.x = rd.uniform(0 + 50, Conf.Window.WIDTH - 50)
            self.y = rd.uniform(0 + 50, Conf.Window.HEIGHT - 50)
            return self.x, self.y

        def get_out_field(self):
            """
            Get coordinates out of field for meteor object
            :return: horizontally and vertically position
            """
            if self.where:
                self.x = rd.choice(
                    (rd.uniform(-self.meteor_size, 0),
                     rd.uniform(Conf.Window.WIDTH, Conf.Window.WIDTH + self.meteor_size)))
                self.y = rd.uniform(-self.meteor_size, Conf.Window.HEIGHT + self.meteor_size)
            else:
                self.x = rd.uniform(-self.meteor_size, Conf.Window.WIDTH + self.meteor_size)
                self.y = rd.choice(
                    (rd.uniform(-self.meteor_size, 0),
                     rd.uniform(Conf.Window.HEIGHT, Conf.Window.HEIGHT + self.meteor_size)))
            return self.x, self.y
