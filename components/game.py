from components.overlay import Overlay
from managers.listener import Event


class Game:
    def __init__(self, window):
        # Environment
        self.window = window
        self.events = []
        # Initialisation

        # Components
        self.comp_overlay = Overlay(self)
        # TODO: Artem

    def reset(self):
        """
        Erases all mobs and objects
        """
        # TODO: Artem

    def start(self):
        """
        Starts the game
        """
        # TODO: Artem

    def event_handler(self, eventName: str):
        """
        Does action from event name
        :param eventName: event name
        """
        # TODO: Artem

    def loop(self, events: list[Event]):
        """
        Do all actions per one frame
        """
        print(list(map(lambda x: x.get_type(), events)))
        # TODO: Artem
