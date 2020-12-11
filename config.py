import pygame as pg


class Configuration:
    """
    Class containing settings of the components
    Don't require creating object
    """
    class Font:
        name = "opensans"

    class Window:
        TITLE = "Space Battle"
        HEIGHT = 700
        WIDTH = 700
        FPS = 60
        POLLING_RATE = 100

    class Game:
        pass

    class Overlay:
        pass

    class Menu:
        HEIGHT = 700
        WIDTH = 700
        GAME_VERSION = "v0.1"
        AUTHORS = "Damir", "Artem", "Dmitriy"
        CONTACTS = ""
        OPACITY = 0

    class Meteor:
        MAX_SIZE = 0
        MIN_SIZE = 0

    class Rocket:
        SIZE = 0

    class Ship:
        SIZE = 0

    class Colors:
        OVERLAY_TXT = "#000000"

    class Rules:
        LIFES = 0
        EVENT_TYPES = [pg.K_w, pg.K_a, pg.K_s, pg.K_d, pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_SPACE, pg.K_RETURN]
