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
        self.size = rd.randint(Conf.Meteor.MIN_SIZE, Conf.Meteor.MAX_SIZE)
        self.raw_image = Img.get_meteor()
        self.count_of_meteor = rd.randint(0, Conf.Images.METEOR[1] - 1)
        w0, h0 = self.raw_image[self.count_of_meteor].get_size()
        scale = self.size / h0
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.image = pg.transform.scale(self.raw_image[self.count_of_meteor], (w1, h1))
        self.rect = self.image.get_rect()
        self.spawn_hor = Conf.Window.WIDTH // 2
        self.spawn_vert = Conf.Window.HEIGHT // 2
        self.move_hor = rd.choice((-1, 1)) * rd.randint(Conf.Meteor.MIN_SPEED, Conf.Meteor.MAX_SPEED)
        self.move_vert = rd.choice((-1, 1)) * rd.randint(Conf.Meteor.MIN_SPEED, Conf.Meteor.MAX_SPEED)
        while Conf.Window.WIDTH // 2 - 100 <= self.spawn_hor <= Conf.Window.WIDTH // 2 + 100:
            self.spawn_hor = rd.randint(self.size, Conf.Window.WIDTH)
        while Conf.Window.HEIGHT // 2 - 100 <= self.spawn_vert <= Conf.Window.HEIGHT // 2 + 100:
            self.spawn_vert = rd.randint(self.size, Conf.Window.HEIGHT)
        self.rect.center = (self.spawn_hor, self.spawn_vert)

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
