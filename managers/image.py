import pygame as pg

from config import Configuration as Conf


class Image:
    """
    Class containing objects' textures, already preparing for using
    """
    SHIP = pg.image.load(f"{Conf.Images.SHIP}.{Conf.Images.FORMAT}")
    ROCKET = pg.image.load(f"{Conf.Images.ROCKET}.{Conf.Images.FORMAT}")
    METEOR = list(
        map(
            lambda x: pg.image.load(f"{x}.{Conf.Images.FORMAT}"),
            range(*Conf.Images.METEOR)
        )
    )
