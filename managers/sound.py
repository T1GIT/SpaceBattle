import pygame as pg

from config import Configuration as Conf


class Sound:
    """
    Class playing sounds of the game
    """
    # TODO: Damir
    def __init__(self):
        pg.mixer.init()

    @staticmethod
    def menu_music():
        pg.mixer.music.load('./resources/sounds/menu/SW-oppening.mp3')
        pg.mixer.music.set_volume(Conf.Sounds.BACKGROUND_MENU)
        pg.mixer.music.play(-1)

    @staticmethod
    def fire_sound():
        fire_sound = pg.mixer.Sound('./resources/sounds/fire/TIEfire.mp3')
        fire_sound.set_volume(Conf.Sounds.FIRE)
        fire_sound.play()

    @staticmethod
    def game_music():
        pg.mixer.music.load('./resources/sounds/bg/kosmos.mp3')
        pg.mixer.music.set_volume(Conf.Sounds.BACKGROUND_GAME)
        pg.mixer.music.play(-1)

    @staticmethod
    def player_explode():
        fire_sound = pg.mixer.Sound('./resources/sounds/explode/Player_explode.mp3')
        fire_sound.set_volume(Conf.Sounds.EXPLODE_ASTEROIDS)
        fire_sound.play()
