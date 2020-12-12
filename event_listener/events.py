import pygame as pg


class Event:
    def __init__(self, eventType: int, data):
        self._type: int = eventType
        self._data = data

    def get_type(self) -> int:
        return self._type

    def get_data(self):
        return self._data


class Mouse:
    class Events:
        BTN = 0
        MOVE = 1

    class Keys:
        LEFT = 0


class Keyboard:
    class Events:
        KEY = 2

    class Keys:
        UP = pg.K_UP
        DOWN = pg.K_DOWN
        LEFT = pg.K_LEFT
        RIGHT = pg.K_RIGHT
        W = pg.K_w
        A = pg.K_a
        S = pg.K_s
        D = pg.K_d
        SPACE = pg.K_SPACE
        ENTER = pg.K_RETURN
        ESC = pg.K_ESCAPE


class Gamepad:
    class Events:
        L_AXIS = 3
        R_AXIS = 4
        KEY = 5

    class Keys:
        A = 0
        B = 1
        RT = 2
        BACK = 6
        START = 7
