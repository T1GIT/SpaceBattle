import pygame as pg
from threading import Thread

from config import Configuration as Conf


class Event:
    def __init__(self, eventType, data):
        self._type = eventType
        self._data = data

    def get_type(self):
        return self._type

    def get_data(self):
        return self._data


class EventTypes:
    MS_BTN = 0
    MS_MV = 1
    KB_KEY = 2
    LS_AXIS = 3
    RS_AXIS = 4
    GP_KEY = 5


class EventListener:
    """
    Collects events in the separated thread.
    Events can be gotten by pop_events(), and
    they will be erasing in the same time.
    """
    __kb_trans = {pg.K_w, pg.K_UP, pg.K_s, pg.K_DOWN, pg.K_a, pg.K_LEFT,
                  pg.K_d, pg.K_RIGHT, pg.K_SPACE, pg.K_RETURN, pg.K_ESCAPE}
    __gp_trans = {

    }

    def __init__(self):
        self._events = []
        self._clock = pg.time.Clock()
        self._running = False
        self._thread = None

    def pop_events(self):
        events = self._events
        self._events = []
        return events

    def listener(self):
        while self._running:
            self._clock.tick(Conf.Window.POLLING_RATE)
            # Mouse checking
            for ms_num, is_pressed in enumerate(pg.mouse.get_pressed(num_buttons=3)):
                if is_pressed:
                    self._events.append(Event(EventTypes.MS_BTN, ms_num))
            rel = pg.mouse.get_rel()
            if rel != (0, 0):
                self._events.append(Event(EventTypes.MS_MV, rel))
            # Keyboard checking
            pressed = pg.key.get_pressed()
            for key in self.__kb_trans:
                if pressed[key]:
                    self._events.append(Event(EventTypes.KB_KEY, rel))
            # Gamepad checking

    def start(self):
        self._running = True
        self._thread = Thread(target=self.listener)
        self._thread.start()

    def is_running(self):
        return self._running

    def stop(self):
        self._running = False
