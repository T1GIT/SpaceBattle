import pygame as pg
from threading import Thread

from config import Configuration as Conf
from event_listener.events import Event, Mouse, Keyboard, Gamepad


class EventListener:
    """
    Collects events in the separated thread.
    Events can be gotten by pop_events(), and
    they will be erasing in the same time.
    """
    __ms_keys = {0}
    __kb_keys = {pg.K_w, pg.K_UP, pg.K_s, pg.K_DOWN, pg.K_a, pg.K_LEFT,
                 pg.K_d, pg.K_RIGHT, pg.K_SPACE, pg.K_RETURN, pg.K_ESCAPE}
    __gp_keys = {0, 1, 6, 7}

    def __init__(self):
        self.__events: list[Event] = []
        self._clock = pg.time.Clock()
        self._thread: Thread = Thread(target=self.listener)
        self._gamepad = None
        self._running: bool = False
        self._interrupted: bool = False

    def start(self):
        self._running = True
        self._thread.start()

    def is_running(self):
        return self._running or not self._interrupted

    def interrupt(self):
        self._interrupted = True

    def pop_events(self):
        events = self.__events
        self.__events = []
        return events

    def listener(self):
        while self._running:
            try:
                self._clock.tick(Conf.Window.POLLING_RATE)
                # Checking devices
                self._check_mouse()
                self._check_keyboard()
                self._check_gamepad()
                for i in self.__events:
                    print(i.get_type())
                # Safe closing thread
                if self._interrupted:
                    self._running = False
            except Exception:
                print("Exception")

    def _check_mouse(self):
        for key in self.__ms_keys:
            if pg.mouse.get_pressed(num_buttons=Conf.EventListener.MOUSE_BUTTONS)[key]:
                event = Event(Mouse.Events.BTN, key)
                self.__events.append(event)
        rel = pg.mouse.get_rel()
        if rel != (0, 0):
            scale = max(map(lambda x: abs(x), rel))
            rel = tuple(map(lambda x: round(x / scale, Conf.EventListener.ACCURACY), rel))
            event = Event(Mouse.Events.MOVE, rel)
            self.__events.append(event)

    def _check_keyboard(self):
        pressed = pg.key.get_pressed()
        for key in self.__kb_keys:
            if pressed[key]:
                event = Event(Keyboard.Events.KEY, key)
                self.__events.append(event)

    def _check_gamepad(self):
        if pg.joystick.get_count() == 0:
            self._gamepad = None
        else:
            if self._gamepad is None:
                self._gamepad = pg.joystick.Joystick(0)
            for btn_num in self.__gp_keys:
                if self._gamepad.get_button(btn_num):
                    event = Event(Gamepad.Events.KEY, btn_num)
                    self.__events.append(event)
            ls_axis = (self._gamepad.get_axis(0), self._gamepad.get_axis(1))
            if any(filter(lambda x: abs(x) > Conf.EventListener.STICK_DEAD_ZONE, ls_axis)):
                data = tuple(map(lambda x: round(x, Conf.EventListener.ACCURACY), ls_axis))
                event = Event(Gamepad.Events.L_AXIS, data)
                self.__events.append(event)
            rs_axis = (self._gamepad.get_axis(3), self._gamepad.get_axis(4))
            if any(filter(lambda x: abs(x) > Conf.EventListener.STICK_DEAD_ZONE, rs_axis)):
                data = tuple(map(lambda x: round(x, Conf.EventListener.ACCURACY), rs_axis))
                event = Event(Gamepad.Events.R_AXIS, data)
                self.__events.append(event)
            z_axis = self._gamepad.get_axis(5)
            if (z_axis + 1) / 2 > Conf.EventListener.TRIGGER_DEAD_ZONE:
                event = Event(Gamepad.Events.KEY, Gamepad.Keys.RT)
                self.__events.append(event)
