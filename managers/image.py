import pygame as pg

from config import Configuration as Conf


class Image:
    """
    Class containing objects' textures, already preparing for using
    """
    __ROOT = "./resources/textures"
    __SHIP = None
    __ROCKET = None
    __METEOR = None

    @staticmethod
    def get_ship() -> pg.image:
        if Image.__SHIP is None:
            Image.__SHIP = pg.image.load(f"{Image.__ROOT}/ship/{Conf.Images.SHIP}.{Conf.Images.FORMAT}").convert_alpha()
        return Image.__SHIP

    @staticmethod
    def get_rocket() -> [pg.image]:
        if Image.__ROCKET is None:
            Image.__ROCKET = []
            for x in range(*Conf.Images.ROCKET):
                Image.__ROCKET.append(pg.image.load(f"{Image.__ROOT}/rocket/{x}.{Conf.Images.FORMAT}").convert_alpha())
        return Image.__ROCKET

    @staticmethod
    def get_meteor() -> [pg.image]:
        if Image.__METEOR is None:
            Image.__METEOR = []
            for x in range(*Conf.Images.METEOR):
                Image.__METEOR.append(pg.image.load(f"{Image.__ROOT}/meteor/{x}.{Conf.Images.FORMAT}").convert_alpha())
        return Image.__METEOR
