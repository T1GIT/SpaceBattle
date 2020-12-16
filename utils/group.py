import pygame as pg

from elements.ship import Ship


class Group:
    ALL = pg.sprite.Group()
    METEORS = pg.sprite.Group()
    ROCKETS = pg.sprite.Group()
    PIECES = pg.sprite.Group()
