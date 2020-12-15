import pygame as pg
import os

import pygame_menu

from config import Configuration as Conf


class Image:
    """
    Class containing objects' images, already prepared for using
    """
    _ROOT = "./resources/images"
    _SHIP = [None, None]
    _ROCKET = None
    _METEORS = None
    _STATIC_BG = None
    _DYNAMIC_BG = None
    _MENU = None
    _ANIMATIONS = dict()

    @staticmethod
    def get_ship(with_fire: bool) -> pg.image:
        if with_fire:
            if Image._SHIP[1] is None:
                Image._SHIP[1] = pg.image.load(
                    f"{Image._ROOT}/ship/{Conf.Images.SHIP}/fire.{Conf.Images.SPRITE_FORMAT}").convert_alpha()
        else:
            if Image._SHIP[0] is None:
                Image._SHIP[0] = pg.image.load(
                    f"{Image._ROOT}/ship/{Conf.Images.SHIP}/normal.{Conf.Images.SPRITE_FORMAT}").convert_alpha()
        return Image._SHIP[1] if with_fire else Image._SHIP[0]

    @staticmethod
    def get_rocket() -> pg.image:
        if Image._ROCKET is None:
            Image._ROCKET = pg.image.load(
                f"{Image._ROOT}/rocket/{Conf.Images.ROCKET}.{Conf.Images.SPRITE_FORMAT}").convert_alpha()
        return Image._ROCKET

    @staticmethod
    def get_meteors() -> [pg.image]:
        if Image._METEORS is None:
            Image._METEORS = []
            path = f"{Image._ROOT}/meteor/{Conf.Images.METEOR}"
            for x in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                Image._METEORS.append(pg.image.load(f"{path}/{x}.{Conf.Images.SPRITE_FORMAT}").convert_alpha())
        return Image._METEORS

    @staticmethod
    def get_static_bg() -> pg.image:
        if Image._STATIC_BG is None:
            Image._STATIC_BG = pg.image.load(
                f"{Image._ROOT}/bg/static/{Conf.Images.STATIC_BG}.{Conf.Images.BASIC_FORMAT}").convert()
        return Image._STATIC_BG

    @staticmethod
    def get_menu() -> pygame_menu.baseimage.BaseImage:
        if Image._MENU is None:
            Image._MENU = pygame_menu.baseimage.BaseImage(
                image_path=f"{Image._ROOT}/bg/menu/{Conf.Images.MENU_BG}.{Conf.Images.BASIC_FORMAT}")
        return Image._MENU

    @staticmethod
    def get_animation(name: str) -> [pg.image]:
        if name not in Image._ANIMATIONS:
            pack = []
            path = f"{Image._ROOT}/anim/{name}"
            for frame in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                pack.append(pg.image.load(f"{path}/{frame}.{Conf.Images.ANIM_FORMAT}").convert_alpha())
            Image._ANIMATIONS.update({name: pack})
        return Image._ANIMATIONS[name]
