import pygame as pg

from config import Configuration as Conf


class Sound:
    """
    Class playing sounds of the game
    """
    _ROOT = "./resources/sounds"
    _VOLUME = Conf.Sound.Volume

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
        fire_sound = pg.mixer.Sound(
            f'{Sound._ROOT}/sfx/shoot/{Conf.Sound.SHOOT}.{Conf.Sound.FORMAT}')
        fire_sound.set_volume(Sound.get_volume(Sound._VOLUME.SHOOT))
        fire_sound.play()

    """
    BACKGROUND
    """
    @staticmethod
    def bg_menu():
        pg.mixer.music.load(
            f'{Sound._ROOT}/background/menu/{Conf.Sound.BG_MENU}.{Conf.Sound.FORMAT}')
        pg.mixer.music.set_volume(Sound.get_volume(Sound._VOLUME.BG_MENU))
        pg.mixer.music.play(-1)

    @staticmethod
    def bg_game():
        pg.mixer.music.load(
            f'{Sound._ROOT}/background/game/{Conf.Sound.BG_GAME}.{Conf.Sound.FORMAT}')
        pg.mixer.music.set_volume(Sound.get_volume(Sound._VOLUME.BG_GAME))
        pg.mixer.music.play(-1)

    """
    EXPLODE
    """
    @staticmethod
    def ex_player():
        fire_sound = pg.mixer.Sound(f'{Sound._ROOT}/explode/player.{Conf.Sound.FORMAT}')
        fire_sound.set_volume(Sound.get_volume(Sound._VOLUME.EX_PLAYER))
        fire_sound.play()

    @staticmethod
    def ex_meteor():
        fire_sound = pg.mixer.Sound(f'{Sound._ROOT}/explode/meteor.{Conf.Sound.FORMAT}')
        fire_sound.set_volume(Sound.get_volume(Sound._VOLUME.EX_METEORS))
        fire_sound.play()
