import pygame as pg
from config import Configuration as Conf
import random as rd
import os


class Meteor(pg.sprite.Sprite):
    """
    Class of the meteor's mobs
    Can destroy ship
    Can be destroyed by rockets
    """
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.textures_folder = os.path.join(os.path.dirname("./resources/textures/"), 'meteor')
        self.size = rd.randint(Conf.Meteor.MIN_SIZE, Conf.Meteor.MAX_SIZE)
        # self.image = pg.Surface((self.size, self.size))
        self.image = pg.image.load(os.path.join(self.textures_folder, f'{rd.randint(0, 4)}.png')).convert()
        # self.image.set_colorkey((255, 255, 255))
        self.rect = pg.transform.scale(self.image, (self.size, self.size)).get_rect()
        self.game.window.screen.blit(self.image, self.rect)
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
