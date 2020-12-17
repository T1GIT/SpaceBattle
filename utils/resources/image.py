import os

import pygame as pg
import pygame_menu

from config import Configuration as Conf


class Image:
    """
    Class containing objects' images, already prepared for using
    """
    _ROOT = "./resources/images"
    SHIPS = None
    ROCKETS = None
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
        if Image.SHIPS is None:
            Image.SHIPS = []
            path = f"{Image._ROOT}/ship"
            for x in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                Image.SHIPS.append([
                    pg.image.load(f"{Image._ROOT}/ship/{x}/normal.{Conf.Image.SPRITE_FORMAT}").convert_alpha(),
                    pg.image.load(f"{Image._ROOT}/ship/{x}/fire.{Conf.Image.SPRITE_FORMAT}").convert_alpha()
                ])
        return Image.SHIPS[Conf.Image.SHIP][1 if with_fire else 0]

    @staticmethod
    def get_rocket() -> pg.image:
        if Image.ROCKETS is None:
            Image.ROCKETS = []
            path = f"{Image._ROOT}/rocket"
            for x in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                Image.ROCKETS.append(pg.image.load(
                    f"{Image._ROOT}/ship/{x}.{Conf.Image.SPRITE_FORMAT}").convert_alpha())
        return Image.ROCKETS[Conf.Image.SHIP]

    @staticmethod
    def get_life() -> pg.image:
        if Image._LIFE is None:
            Image._LIFE = pg.image.load(
                f"{Image._ROOT}/life/{Conf.Image.LIFE}.{Conf.Image.SPRITE_FORMAT}").convert_alpha()
        return Image._LIFE

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
