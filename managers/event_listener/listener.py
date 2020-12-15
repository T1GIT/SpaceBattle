import pygame as pg
from math import pow

from config import Configuration as Conf
from managers.event_listener.events import Event, Mouse, Keyboard, Gamepad


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
    _stick_sens = (11 - Conf.EventListener.STICK_SENSITIVITY) * 2 / 10

    @staticmethod
    def get_events():
        """
        Main thread's cycle.
        Checks devices state, writes events if it has them
        Can be safely closed by calling <EventListener.object>.interrupt()
        """
        events = dict()
        # Checking devices
        events["system"] = EventListener._check_system()
        events["mouse"] = EventListener._check_mouse()
        events["keyboard"] = EventListener._check_keyboard()
        events["gamepad"] = EventListener._check_gamepad()
        return events

    @staticmethod
    def _check_system():
        events = []
        for event_type in EventListener._system:
            if pg.event.peek(event_type):
                event = Event(pg.QUIT, None)
                events.append(event)
        return events

    @staticmethod
    def _check_mouse():
        """
        Checks mouse buttons' state, mouse motion
        and collects it.
        """
        events = []
        for key in EventListener._ms_keys:
            if pg.mouse.get_pressed(num_buttons=Conf.EventListener.MOUSE_BUTTONS)[key]:
                events.append(Event(Mouse.Events.KEY, key))
        rel = pg.mouse.get_rel()
        if rel != (0, 0):
            events.append(Event(Mouse.Events.MOVE, (rel[0], -rel[1])))
        return events

    @staticmethod
    def _check_keyboard():
        """
        Checks keyboard buttons' state
        and collects pressed keys.
        """
        events = []
        pressed = pg.key.get_pressed()
        for key in EventListener._kb_keys:
            if pressed[key]:
                events.append(Event(Keyboard.Events.KEY, key))
        return events

    @staticmethod
    def _check_gamepad():
        """
        Checks gamepad buttons' and sticks' state
        and collects it.
        """
        events = []
        if pg.joystick.get_count() == 0:
            EventListener._gamepad = None
        else:
            if EventListener._gamepad is None:
                EventListener._gamepad = pg.joystick.Joystick(0)
            for btn_num in EventListener._gp_keys:
                if EventListener._gamepad.get_button(btn_num):
                    events.append(Event(Gamepad.Events.KEY, btn_num))
            l_x, l_y = (EventListener._gamepad.get_axis(0), -EventListener._gamepad.get_axis(1))
            if abs(l_x) > Conf.EventListener.STICK_DEAD_ZONE or abs(l_y) > Conf.EventListener.STICK_DEAD_ZONE:
                events.append(Event(Gamepad.Events.LS, EventListener._get_axis(l_x, l_y)))
            r_x, r_y = (EventListener._gamepad.get_axis(3), -EventListener._gamepad.get_axis(4))
            if abs(r_x) > Conf.EventListener.STICK_DEAD_ZONE or abs(r_y) > Conf.EventListener.STICK_DEAD_ZONE:
                events.append(Event(Gamepad.Events.RS, EventListener._get_axis(r_x, r_y)))
            z_axis = EventListener._gamepad.get_axis(5)
            if (z_axis + 1) / 2 > Conf.EventListener.TRIGGER_DEAD_ZONE:
                events.append(Event(Gamepad.Events.KEY, Gamepad.Keys.RT))
        return events

    @staticmethod
    def _get_axis(x, y):
        x = pow(abs(x), EventListener._stick_sens) * (-1 if x < 0 else 1)
        y = pow(abs(y), EventListener._stick_sens) * (-1 if y < 0 else 1)
        return x, y
