import pygame as pg

from config import Configuration as Conf


class Sound:
    """
    Class playing sounds of the game
    """
    _ROOT = "./resources/sounds"
    _VOLUME = Conf.Sound.Volume
    _SHOOT = None
    _EX_PLAYER = None
    _EX_METEOR = None

    @staticmethod
    def get_volume(volume: float) -> float:
        return volume * Conf.Sound.Volume.GENERAL / 100

    """
    SFX
    """
    @staticmethod
    def click():
        return f"{Sound._ROOT}/sfx/click/{Conf.Sound.CLICK}.{Conf.Sound.FORMAT}"

    @staticmethod
    def shoot():
        if Sound._SHOOT is None:
            Sound._SHOOT = pg.mixer.Sound(
                f'{Sound._ROOT}/sfx/shoot/{Conf.Sound.SHOOT}.{Conf.Sound.FORMAT}')
            Sound._SHOOT.set_volume(Sound.get_volume(Sound._VOLUME.SFX))
        Sound._SHOOT.play()

    """
    BACKGROUND
    """
    @staticmethod
    def bg_menu():
        pg.mixer.music.load(
            f'{Sound._ROOT}/background/menu/{Conf.Sound.BG_MENU}.{Conf.Sound.FORMAT}')
        pg.mixer.music.set_volume(Sound.get_volume(Sound._VOLUME.BG))
        pg.mixer.music.play(-1)

    @staticmethod
    def bg_game():
        pg.mixer.music.load(
            f'{Sound._ROOT}/background/game/{Conf.Sound.BG_GAME}.{Conf.Sound.FORMAT}')
        pg.mixer.music.set_volume(Sound.get_volume(Sound._VOLUME.BG))
        pg.mixer.music.play(-1)

    """
    EXPLODE
    """
    @staticmethod
    def ex_player():
        if Sound._EX_PLAYER is None:
            Sound._EX_PLAYER = pg.mixer.Sound(f'{Sound._ROOT}/explode/player.{Conf.Sound.FORMAT}')
            Sound._EX_PLAYER.set_volume(Sound.get_volume(Sound._VOLUME.SFX))
        Sound._EX_PLAYER.play()

    @staticmethod
    def ex_meteor():
        if Sound._EX_METEOR is None:
            Sound._EX_METEOR = pg.mixer.Sound(f'{Sound._ROOT}/explode/meteor.{Conf.Sound.FORMAT}')
            Sound._EX_METEOR.set_volume(Sound.get_volume(Sound._VOLUME.SFX))
        Sound._EX_METEOR.play()

    class Volume:

        @staticmethod
        def set_general(level: float):
            pass

        @staticmethod
        def set_sfx(level: float):
            pass

        @staticmethod
        def set_bg(level: float):
            pass

