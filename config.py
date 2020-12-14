class Configuration:
    """
    Class containing settings of the components
    Don't require creating object
    """
    class Window:
        TITLE = "Space Battle"
        FULLSCREEN = True
        WIDTH = 1000
        HEIGHT = 1000
        BLUR = True

    class Game:
        pass

    class Overlay:
        pass

    class Menu:
        GAME_VERSION = "v0.1"
        AUTHORS = "Damir", "Artem", "Dmitriy"
        CONTACTS = ""
        OPACITY = 0

        class Title:
            X_OFFSET = 100
            Y_OFFSET = 40
            SIZE = 70

    class Font:
        name = "opensans"

    class DynamicBG:
        OPACITY = 50  # [0, 100]

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
        QUANTITY = 100
        BY_TIME = False
        PERIOD = 1000
        ON_FIELD = False

    class Rocket:
        SIZE = 5  # px
        SPEED = 2  # > 0
        PERIOD = 100  # ms
        MAX_DISTANCE = 300  # px  (needs Rocket.UNLIMITED = False)
        UNLIMITED = True

    class Colors:
        OVERLAY_TXT = "#000000"

    class Images:
        SHIP = 0
        ROCKET = 1
        METEOR = 0
        STATIC_BG = 0
        DYNAMIC_BG = 0
        FORMAT = "png"
        BASIC_FORMAT = "jpg"

    class Sounds:
        FIRE = 0.3
        BACKGROUND_GAME = 0.1
        BACKGROUND_MENU = 0.1
        CLICK = 0.1
        EXPLODE_PLAYER = 0.5
        EXPLODE_ASTEROIDS = 0.2

    class EventListener:
        MOUSE_BUTTONS = 3
        STICK_SENSITIVITY = 2  # [1; 10]
        STICK_DEAD_ZONE = 0.2
        TRIGGER_DEAD_ZONE = 0.5

    class Rules:
        FPS = 60
        POLLING_RATE = 60
        LIFES = 0

    # Checking parameters
    assert 0 <= EventListener.STICK_SENSITIVITY <= 10
    assert 1 <= Ship.ACCURACY <= 10
    assert 0 < Ship.RESIST < 1
    assert Rules.POLLING_RATE <= Rules.FPS
    assert Ship.SMOOTH >= 1
    assert Meteor.MAX_SIZE >= Meteor.MIN_SIZE
    assert Rocket.SPEED > 0
    assert 0 <= DynamicBG.OPACITY <= 100

