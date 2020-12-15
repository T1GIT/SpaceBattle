import pygame as pg


class Mouse:
    class Events:
        KEY = 0
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
        LS = 3
        RS = 4
        KEY = 5

    class Keys:
        A = 0
        B = 1
        RT = 2
        BACK = 6
        START = 7
