import pygame as pg
import os

import pygame_menu

from config import Configuration as Conf


class Image:
    """
    Class containing objects' images, already prepared for using
    """
    __ROOT = "./resources/images"
    __SHIP = [None, None]
    __ROCKET = None
    __METEORS = None
    __STATIC_BG = None
    __DYNAMIC_BG = None
    __MENU = None
    __EXPLOSION = None

    @staticmethod
    def get_ship(with_fire: bool) -> pg.image:
        if with_fire:
            if Image.__SHIP[1] is None:
                Image.__SHIP[1] = pg.image.load(
                    f"{Image.__ROOT}/ship/{Conf.Images.SHIP}/fire.{Conf.Images.SPRITE_FORMAT}").convert_alpha()
        else:
            if Image.__SHIP[0] is None:
                Image.__SHIP[0] = pg.image.load(
                    f"{Image.__ROOT}/ship/{Conf.Images.SHIP}/normal.{Conf.Images.SPRITE_FORMAT}").convert_alpha()
        return Image.__SHIP[1] if with_fire else Image.__SHIP[0]

    @staticmethod
    def get_rocket() -> pg.image:
        if Image.__ROCKET is None:
            Image.__ROCKET = pg.image.load(
                f"{Image.__ROOT}/rocket/{Conf.Images.ROCKET}.{Conf.Images.SPRITE_FORMAT}").convert_alpha()
        return Image.__ROCKET

    @staticmethod
    def get_meteors() -> [pg.image]:
        if Image.__METEORS is None:
            Image.__METEORS = []
            path = f"{Image.__ROOT}/meteor/{Conf.Images.METEOR}"
            for x in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                Image.__METEORS.append(pg.image.load(f"{path}/{x}.{Conf.Images.SPRITE_FORMAT}").convert_alpha())
        return Image.__METEORS

    @staticmethod
    def get_static_bg() -> pg.image:
        if Image.__STATIC_BG is None:
            Image.__STATIC_BG = pg.image.load(
                f"{Image.__ROOT}/bg/static/{Conf.Images.STATIC_BG}.{Conf.Images.BASIC_FORMAT}").convert()
        return Image.__STATIC_BG

    @staticmethod
    def get_menu() -> pygame_menu.baseimage.BaseImage:
        if Image.__MENU is None:
            Image.__MENU = pygame_menu.baseimage.BaseImage(
                image_path=f"{Image.__ROOT}/bg/menu/{Conf.Images.MENU_BG}.{Conf.Images.BASIC_FORMAT}")
        return Image.__MENU

    @staticmethod
    def get_explosion() -> [pg.image]:
        if Image.__EXPLOSION is None:
            Image.__EXPLOSION = []
            path = f"{Image.__ROOT}/gif/explosion"
            for frame in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                Image.__EXPLOSION.append(pg.image.load(f"{path}/{frame}.{Conf.Images.ANIM_FORMAT}").convert_alpha())
        return Image.__EXPLOSION
