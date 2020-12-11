import pygame as pg

from config import Configuration as Conf


class Image:
    """
    Class containing objects' textures, already preparing for using
    """
    SHIP = pg.image.load(f"./resources/textures/ship/{Conf.Images.SHIP}.{Conf.Images.FORMAT}").convert_alpha()
    ROCKET = pg.image.load(f"./resources/textures/rocket/{Conf.Images.ROCKET}.{Conf.Images.FORMAT}").convert_alpha()
    METEOR = list(
        map(
            lambda x: pg.image.load(f"./resources/textures/meteor/{x}.{Conf.Images.FORMAT}").convert_alpha(),
            range(*Conf.Images.METEOR)
        )
    )

