class Configuration:
    """
    Class containing settings of the components
    Don't require creating object
    """
    class Window:
        TITLE = "Space Battle"
        HEIGHT = 700
        WIDTH = 700
        FPS = 60

    class Game:
        pass

    class Overlay:
        pass

    class Menu:
        WIDTH = 0
        HEIGHT = 0
        OPACITY = 0

    class Meteor:
        MAX_SIZE = 0
        MIN_SIZE = 0

    class Rocket:
        SIZE = 0

    class Ship:
        SIZE = 0

    class Colors:
        OVERLAY_TXT = "#000000"

    class Rules:
        LIFES = 0
