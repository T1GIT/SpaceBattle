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
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.raw_image = Img.get_meteor()
        self.count_rotate = 0
        self.count_of_meteor = rd.randint(0, len(self.raw_image) - 1)
        w0, h0 = self.raw_image[self.count_of_meteor].get_size()
        scale = rd.randint(Conf.Meteor.MIN_SIZE, Conf.Meteor.MAX_SIZE) / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.image = pg.transform.scale(self.raw_image[self.count_of_meteor], (w1, h1))
        self.copy_image = self.image.copy()
        self.move_hor = rd.choice((-1, 1)) * rd.randint(Conf.Meteor.MIN_SPEED, Conf.Meteor.MAX_SPEED)
        self.move_vert = rd.choice((-1, 1)) * rd.randint(Conf.Meteor.MIN_SPEED, Conf.Meteor.MAX_SPEED)
        self.angle = 0
        self.angle_speed = rd.randint(-5, 5)

    def rotate(self):
        """
        Rotate the figure
        """
        self.angle = (self.angle + self.angle_speed) % 360
        old_center = self.rect.center
        new_image = pg.transform.rotate(self.image, self.angle)
        self.rect = new_image.get_rect(center=old_center)
        self.game.window.screen.blit(new_image, self.rect)

    def locate(self, x, y):
        """
        Shows sprite in the screen
        :param x: position
        :param y: position
        """
        self.rect = self.copy_image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += self.move_hor
        self.rect.y += self.move_vert
        if self.rect.left > Conf.Window.WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = Conf.Window.WIDTH
        if self.rect.top > Conf.Window.HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = Conf.Window.HEIGHT
        self.rotate()
