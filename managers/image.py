import pygame as pg
import os

from config import Configuration as Conf


class Image:
    """
    Class containing objects' textures, already prepared for using
    """
    __ROOT = "./resources/textures"
    __SHIP = [None, None]
    __ROCKET = None
    __METEOR = None

    @staticmethod
    def get_ship(with_fire: bool) -> pg.image:
        if with_fire:
            if Image.__SHIP[1] is None:
                Image.__SHIP[1] = pg.image.load(
                    f"{Image.__ROOT}/ship/{Conf.Images.SHIP}/fire.{Conf.Images.FORMAT}").convert_alpha()
        else:
            if Image.__SHIP[0] is None:
                Image.__SHIP[0] = pg.image.load(
                    f"{Image.__ROOT}/ship/{Conf.Images.SHIP}/normal.{Conf.Images.FORMAT}").convert_alpha()
        return Image.__SHIP[1 if with_fire else 0]

    @staticmethod
    def get_rocket() -> pg.image:
        if Image.__ROCKET is None:
            Image.__ROCKET = pg.image.load(
                f"{Image.__ROOT}/rocket/{Conf.Images.ROCKET}.{Conf.Images.FORMAT}").convert_alpha()
        return Image.__ROCKET

    @staticmethod
    def get_meteors() -> [pg.image]:
        if Image.__METEOR is None:
            Image.__METEOR = []
            path = f"{Image.__ROOT}/meteor/{Conf.Images.METEOR}"
            for x in range(len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])):
                Image.__METEOR.append(pg.image.load(f"{path}/{x}.{Conf.Images.FORMAT}").convert_alpha())
        return Image.__METEOR
