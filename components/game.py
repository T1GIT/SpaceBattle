from components.overlay import Overlay


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

    def add_event(self, eventName: str):
        self.events.append(eventName)

    def loop(self):
        """
        Do all actions per one frame
        """
        # TODO: Artem
