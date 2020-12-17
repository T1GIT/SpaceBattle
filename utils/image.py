import os

import pygame as pg
import pygame_menu

from config import Configuration as Conf


class Image:
    """
    Class containing objects' images, already prepared for using
    """
    _ROOT = "./resources/images"
    _SHIP = [None, None]
    _FIGHTER = None
    _ROCKET = None
    _METEORS = None
    _BACKGROUND = None
    _PIECES = None
    _MENU = None
    _LIFE = None
    _ANIMATIONS = dict()

    @staticmethod
    def get_menu() -> pygame_menu.baseimage.BaseImage:
        if Image._MENU is None:
            Image._MENU = pygame_menu.baseimage.BaseImage(
                image_path=f"{Image._ROOT}/bg/menu/{Conf.Image.MENU_BG}.{Conf.Image.BASIC_FORMAT}")
        return Image._MENU

    @staticmethod
    def get_ship(with_fire: bool) -> pg.image:
        if with_fire:
            if Image._SHIP[1] is None:
                Image._SHIP[1] = pg.image.load(
                    f"{Image._ROOT}/ship/{Conf.Image.SHIP}/fire.{Conf.Image.SPRITE_FORMAT}").convert_alpha()
        else:
            if Image._SHIP[0] is None:
                Image._SHIP[0] = pg.image.load(
                    f"{Image._ROOT}/ship/{Conf.Image.SHIP}/normal.{Conf.Image.SPRITE_FORMAT}").convert_alpha()
        return Image._SHIP[1] if with_fire else Image._SHIP[0]

    @staticmethod
    def get_life() -> pg.image:
        if Image._LIFE is None:
            Image._LIFE = pg.image.load(
                f"{Image._ROOT}/life/{Conf.Image.LIFE}.{Conf.Image.SPRITE_FORMAT}").convert_alpha()
        return Image._LIFE

    @staticmethod
    def get_rocket() -> pg.image:
        if Image._ROCKET is None:
            Image._ROCKET = pg.image.load(
                f"{Image._ROOT}/rocket/{Conf.Image.ROCKET}.{Conf.Image.SPRITE_FORMAT}").convert_alpha()
        return Image._ROCKET

    @staticmethod
    def get_fighter() -> pg.image:
        if Image._FIGHTER is None:
            Image._FIGHTER = pg.image.load(
                f"{Image._ROOT}/enemy/fighter.{Conf.Image.SPRITE_FORMAT}").convert_alpha()
        return Image._FIGHTER

    @staticmethod
    def get_background() -> pg.image:
        if Image._BACKGROUND is None:
            Image._BACKGROUND = pg.image.load(
                f"{Image._ROOT}/bg/static/{Conf.Image.STATIC_BG}.{Conf.Image.BASIC_FORMAT}").convert()
        return Image._BACKGROUND

    @staticmethod
    def get_meteors() -> [pg.image]:
        if Image._METEORS is None:
            Image._METEORS = []
            path = f"{Image._ROOT}/meteor"
            for x in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                Image._METEORS.append(pg.image.load(f"{path}/{x}.{Conf.Image.SPRITE_FORMAT}").convert_alpha())
        return Image._METEORS

    @staticmethod
    def get_animation(name: str) -> [pg.image]:
        if name not in Image._ANIMATIONS:
            pack = []
            path = f"{Image._ROOT}/anim/{name}"
            for frame in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                pack.append(pg.image.load(f"{path}/{frame}.{Conf.Image.ANIM_FORMAT}").convert_alpha())
            Image._ANIMATIONS.update({name: pack})
        return Image._ANIMATIONS[name]

    @staticmethod
    def get_pieces() -> [pg.image]:
        if Image._PIECES is None:
            Image._PIECES = []
            path = f"{Image._ROOT}/piece"
            for x in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                print()
                Image._PIECES.append(pg.image.load(f"{path}/{x}.{Conf.Image.SPRITE_FORMAT}").convert_alpha())
        return Image._PIECES
