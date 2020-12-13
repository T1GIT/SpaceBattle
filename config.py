class Configuration:
    """
    Class containing settings of the components
    Don't require creating object
    """
    class Window:
        TITLE = "Space Battle"
        FULLSCREEN = False
        WIDTH = 700
        HEIGHT = 700
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

    class Font:
        name = "opensans"

    class Ship:
        SIZE = 100
        WEIGHT = 2
        POWER = 5
        RESIST = 0.05  # (0; 1)
        SMOOTH = 8  # >= 1
        ACCURACY = 5  # [1; 10]

    class Meteor:
        MAX_SIZE = 100
        MIN_SIZE = 50
        MIN_SPEED = 1
        MAX_SPEED = 2
        MAX_ROTATE_SPEED = 5
        QUANTITY = 10

    class Rocket:
        SIZE = 5  # px
        SPEED = 2  # > 0
        PERIOD = 100  # ms
        MAX_DISTANCE = 300  # px  (needs Rocket.UNLIMITED = False)
        UNLIMITED = True

    class Colors:
        OVERLAY_TXT = "#000000"

    class Images:
        SHIP = 1
        ROCKET = 1
        METEOR = 0
        FORMAT = "png"

    class EventListener:
        MOUSE_BUTTONS = 3
        STICK_SENSITIVITY = 2  # [1; 10]
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
    assert Meteor.MAX_SIZE >= Meteor.MIN_SIZE
    assert Rocket.SPEED > 0

