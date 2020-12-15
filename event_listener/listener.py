from math import pow
from threading import Thread

import pygame as pg

from config import Configuration as Conf
from event_listener.events import Mouse, Keyboard, Gamepad


class EventListener:
    """
    Collects events in the separated thread.
    Events can be gotten by pop_events(), and
    they will be erasing in the same time.
    """
    _ms_keys = {0}
    _kb_keys = {pg.K_w, pg.K_UP, pg.K_s, pg.K_DOWN, pg.K_a, pg.K_LEFT,
                pg.K_d, pg.K_RIGHT, pg.K_SPACE, pg.K_RETURN, pg.K_ESCAPE}
    _gp_keys = {0, 1, 6, 7}
    _system = {pg.QUIT}

    def __init__(self):
        self._events: dict = dict()
        self._thread: Thread = Thread(target=self._listener)
        self._clock = pg.time.Clock()
        self._gamepad = None
        self._stick_sens = (11 - Conf.EventListener.STICK_SENSITIVITY) * 2 / 10
        self._running: bool = False
        self._interrupted: bool = False

    def start(self):
        """
        Starts the thread
        """
        self._running = True
        self._thread.start()

    def is_running(self) -> bool:
        """
        Checks if the thread is working
        :return: True if the thread isn't finished
        """
        return self._running or not self._interrupted

    def interrupt(self):
        """
        Turn on flag for the thread to finish
        """
        self._interrupted = True

    def get_events(self) -> dict:
        """
        Returns events for the current time
        :return: events dict
        """
        return self._events

    def erase(self):
        self._events = dict()

    def _listener(self):
        """
        Main thread's cycle.
        Checks devices state, writes events if it has them
        Can be safely closed by calling <EventListener.object>.interrupt()
        """
        while self._running:
            # Checking devices
            self._check_system()
            self._check_mouse()
            self._check_keyboard()
            self._check_gamepad()
            # Safe closing thread
            if self._interrupted:
                self._running = False
            self._clock.tick(Conf.Rules.POLLING_RATE)

    def _check_system(self):
        for event_type in self._system:
            if pg.event.peek(event_type):
                self._events[event_type] = None

    def _check_mouse(self):
        """
        Checks mouse buttons' state, mouse motion
        and collects it.
        """
        for key in self._ms_keys:
            if pg.mouse.get_pressed(num_buttons=Conf.EventListener.MOUSE_BUTTONS)[key]:
                self._events[Mouse.Events.KEY] = key
        rel = pg.mouse.get_rel()
        if rel != (0, 0):
            self._events[Mouse.Events.MOVE] = (rel[0], -rel[1])

    def _check_keyboard(self):
        """
        Checks keyboard buttons' state
        and collects pressed keys.
        """
        pressed = pg.key.get_pressed()
        for key in self._kb_keys:
            if pressed[key]:
                self._events[Keyboard.Events.KEY] = key

    def _check_gamepad(self):
        """
        Checks gamepad buttons' and sticks' state
        and collects it.
        """
        if pg.joystick.get_count() == 0:
            self._gamepad = None
        else:
            if self._gamepad is None:
                self._gamepad = pg.joystick.Joystick(0)
            for btn_num in self._gp_keys:
                if self._gamepad.get_button(btn_num):
                    self._events[Gamepad.Events.KEY] = btn_num
            l_x, l_y = (self._gamepad.get_axis(0), -self._gamepad.get_axis(1))
            if abs(l_x) > Conf.EventListener.STICK_DEAD_ZONE or abs(l_y) > Conf.EventListener.STICK_DEAD_ZONE:
                self._events[Gamepad.Events.LS] = self._get_axis(l_x, l_y)
            r_x, r_y = (self._gamepad.get_axis(3), -self._gamepad.get_axis(4))
            if abs(r_x) > Conf.EventListener.STICK_DEAD_ZONE or abs(r_y) > Conf.EventListener.STICK_DEAD_ZONE:
                self._events[Gamepad.Events.RS] = self._get_axis(r_x, r_y)
            z_axis = self._gamepad.get_axis(5)
            if (z_axis + 1) / 2 > Conf.EventListener.TRIGGER_DEAD_ZONE:
                self._events[Gamepad.Events.KEY] = Gamepad.Keys.RT

    def _get_axis(self, x, y):
        x = pow(abs(x), self._stick_sens) * (-1 if x < 0 else 1)
        y = pow(abs(y), self._stick_sens) * (-1 if y < 0 else 1)
        return x, y
