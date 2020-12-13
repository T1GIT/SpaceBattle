import pygame as pg
from threading import Thread
from math import pow

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
        self.__events: [Event] = []
        self._thread: Thread = Thread(target=self.listener)
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

    def pop_events(self) -> list[Event]:
        """
        Returns events list collected in for the current
        time and erases them after
        :return: events list
        """
        events = self.__events
        self.__events = []
        return events

    def listener(self):
        """
        Main thread's cycle.
        Checks devices state, writes events if it has them
        Can be safely closed by calling <EventListener.object>.interrupt()
        """
        while self._running:
            try:
                self._clock.tick(Conf.Window.POLLING_RATE)
                # Checking devices
                self._check_mouse()
                self._check_keyboard()
                self._check_gamepad()
                # Safe closing thread
                if self._interrupted:
                    self._running = False
            except Exception:
                print("Was catch in the EventListener cycle")

    def _check_mouse(self):
        """
        Checks mouse buttons' state, mouse motion
        and collects it.
        """
        for key in self.__ms_keys:
            if pg.mouse.get_pressed(num_buttons=Conf.EventListener.MOUSE_BUTTONS)[key]:
                event = Event(Mouse.Events.KEY, key)
                self.__events.append(event)
        rel = pg.mouse.get_rel()
        if rel != (0, 0):
            event = Event(Mouse.Events.MOVE, (rel[0], -rel[1]))
            self.__events.append(event)

    def _check_keyboard(self):
        """
        Checks keyboard buttons' state
        and collects pressed keys.
        """
        pressed = pg.key.get_pressed()
        for key in self.__kb_keys:
            if pressed[key]:
                event = Event(Keyboard.Events.KEY, key)
                self.__events.append(event)

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
            for btn_num in self.__gp_keys:
                if self._gamepad.get_button(btn_num):
                    event = Event(Gamepad.Events.KEY, btn_num)
                    self.__events.append(event)
            l_x, l_y = (self._gamepad.get_axis(0), -self._gamepad.get_axis(1))
            if abs(l_x) > Conf.EventListener.STICK_DEAD_ZONE or abs(l_y) > Conf.EventListener.STICK_DEAD_ZONE:
                event = Event(Gamepad.Events.LS, self.__get_axis(l_x, l_y))
                self.__events.append(event)
            r_x, r_y = (self._gamepad.get_axis(3), -self._gamepad.get_axis(4))
            if abs(r_x) > Conf.EventListener.STICK_DEAD_ZONE or abs(r_y) > Conf.EventListener.STICK_DEAD_ZONE:
                event = Event(Gamepad.Events.RS, self.__get_axis(r_x, r_y))
                self.__events.append(event)
            z_axis = self._gamepad.get_axis(5)
            if (z_axis + 1) / 2 > Conf.EventListener.TRIGGER_DEAD_ZONE:
                event = Event(Gamepad.Events.KEY, Gamepad.Keys.RT)
                self.__events.append(event)

    def __get_axis(self, x, y):
        x = pow(abs(x), self._stick_sens) * (-1 if x < 0 else 1)
        y = pow(abs(y), self._stick_sens) * (-1 if y < 0 else 1)
        return x, y
