import pygame as pg
from config import Configuration as Conf
import random as rd
from managers.image import Image as Img


class Animation(pg.sprite.Sprite):
    """
    """
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        raw_image = Img.get_meteors()
        self.count_rotate = 0
        self.count_of_meteor = rd.randint(0, len(raw_image) - 1)
        w0, h0 = raw_image[self.count_of_meteor].get_size()
        scale = rd.randint(Conf.Meteor.MIN_SIZE, Conf.Meteor.MAX_SIZE) / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.texture = pg.transform.scale(raw_image[self.count_of_meteor], (w1, h1))
        self.image = self.texture.copy()
        self.speed_x = rd.choice((-1, 1)) * rd.randint(Conf.Meteor.MIN_SPEED, Conf.Meteor.MAX_SPEED)
        self.speed_y = rd.choice((-1, 1)) * rd.randint(Conf.Meteor.MIN_SPEED, Conf.Meteor.MAX_SPEED)
        self.angle = 0
        self.angle_speed = rd.randint(1, Conf.Meteor.MAX_ROTATE_SPEED) * rd.choice((-1, 1))

    def locate(self, x, y):
        """
        Shows sprite in the screen
        :param x: position of the end
        :param y: position of the end
        """
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):

