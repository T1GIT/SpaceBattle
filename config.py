class Configuration:
    """
    Class containing settings of the components
    Don't require creating object
    """
    class Font:
        name = "opensans"

    class Window:
        TITLE = "Space Battle"
        FULLSCREEN = True
        HEIGHT = 700
        WIDTH = 700
        FPS = 60
        POLLING_RATE = 60

    class Game:
        pass

    class Overlay:
        pass

    class Menu:
        HEIGHT = 700
        WIDTH = 700
        GAME_VERSION = "v0.1"
        AUTHORS = "Damir", "Artem", "Dmitriy"
        CONTACTS = ""
        OPACITY = 0

    class Meteor:
        MAX_SIZE = 60
        MIN_SIZE = 30
        MIN_SPEED = 1
        MAX_SPEED = 2
        QUANTITY = 10

    class Rocket:
        SIZE = 5
        LIFE = 150

    class Ship:
        SIZE = 200
        WEIGHT = 5
        POWER = 5
        RESIST = 0.05  # (0; 1)
        SMOOTH = 8  # >= 1
        ACCURACY = 3  # [1; 10]

    class Colors:
        OVERLAY_TXT = "#000000"

    class Images:
        SHIP = 0
        ROCKET = 0
        METEOR = 0
        FORMAT = "png"

    class EventListener:
        MOUSE_BUTTONS = 3
        STICK_SENSITIVITY = 5  # [1; 10]
        STICK_DEAD_ZONE = 0.2
        TRIGGER_DEAD_ZONE = 0.5

    class Rules:
        LIFES = 0

    # Checking parameters
    assert 0 <= EventListener.STICK_SENSITIVITY <= 10
    assert 1 <= Ship.ACCURACY <= 10
    assert 0 < Ship.RESIST < 1
    assert Window.POLLING_RATE <= Window.FPS
    assert Ship.SMOOTH >= 1

