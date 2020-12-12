import pygame as pg


class Configuration:
    """
    Class containing settings of the components
    Don't require creating object
    """
    class Window:
        TITLE = "Space Battle"
        HEIGHT = 700
        WIDTH = 700
        FPS = 60
        POLLING_RATE = 20

    class Game:
        pass

    class Overlay:
        pass

    class Menu:
        WIDTH = 0
        HEIGHT = 0
        OPACITY = 0

    class Meteor:
        MAX_SIZE = 60
        MIN_SIZE = 30
        MIN_SPEED = 1
        MAX_SPEED = 2

    class Rocket:
        SIZE = 10

    class Ship:
        SIZE = 100

    class Colors:
        OVERLAY_TXT = "#000000"

    class Images:
        SHIP = 0
        ROCKET = (0, 4)
        METEOR = (0, 5)
        FORMAT = "png"

    class EventListener:
        ACCURACY = 1
        MOUSE_BUTTONS = 3
        STICK_DEAD_ZONE = 0.2
        TRIGGER_DEAD_ZONE = 0.5

    class Rules:
        LIFES = 0
