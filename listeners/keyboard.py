import pygame as pg
from threading import Thread

from config import Configuration as Conf


class GamepadListener:
    def __init__(self):
        self.events = []
        self._clock = pg.time.Clock()
        self._running = False
        self._thread = None

    def listener(self):
        self._clock.tick(Conf.Window.POLLING_RATE)
        pressed = pg.key.get_pressed()
        while self._running:
            for event_type in Conf.Rules.EVENT_TYPES:
                if event_type in pressed:
                    self.events.append(event_type)

    def erase(self):
        self.events = []

    def start(self):
        self._running = True
        self._thread = Thread()
        self._thread.start()

    def stop(self):
        self._running = False
