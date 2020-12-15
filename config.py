class Configuration:
    """
    Class containing settings of the components
    Don't require creating object
    """
    class Window:
        TITLE = "Space Battle"
        FULLSCREEN = False
        WIDTH = 1000
        HEIGHT = 1000

    class Game:
        pass

    class Overlay:
        TXT_COLOR = "#000000"

    class Menu:
        GAME_VERSION = "v0.1"
        AUTHORS = "Damir", "Artem", "Dmitriy"
        CONTACTS = ""
        THEME_COLOR = (0, 250, 0)

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
        SMOOTH = 10  # >= 1
        ACCURACY = 5  # [1; 10]
        DEAD_SPEED = 0.2

    class Meteor:
        MAX_SIZE = 100
        MIN_SIZE = 50
        MIN_SPEED = 0.5
        MAX_SPEED = 3
        ROTATING = True
        MIN_ROTATE_SPEED = 1
        MAX_ROTATE_SPEED = 5
        QUANTITY = 10
        BY_TIME = False
        PERIOD = 1000
        ON_FIELD = True

    class Rocket:
        SIZE = 10  # px
        SPEED = 20  # > 0
        PERIOD = 200  # ms
        MAX_DISTANCE = 300  # px  (needs Rocket.UNLIMITED = False)
        UNLIMITED = True

    class Animation:
        SIZE = 100
        FPS = 30

    class Images:
        SHIP = 0
        ROCKET = 1
        METEOR = 0
        MENU_BG = 0
        STATIC_BG = 0
        DYNAMIC_BG = 0
        ANIM_FORMAT = "gif"
        SPRITE_FORMAT = "png"
        BASIC_FORMAT = "jpg"

    class Sound:
        SHOOT = 0
        CLICK = 0
        BG_MENU = 0
        BG_GAME = 0
        FORMAT = "mp3"

        class Volume:
            GENERAL = 5  # [0; 10]
            BG = 7  # [0; 10]
            SFX = 5  # [0; 10]

    class Control:
        MOUSE_BUTTONS = 3
        STICK_SENSITIVITY = 2  # [1; 10]
        STICK_DEAD_ZONE = 0.2
        TRIGGER_DEAD_ZONE = 0.5

    class Rules:
        FPS = 60
        GAME_SPEED = 60
        SCALE = GAME_SPEED / FPS
        LIVES = 0

    # Checking parameters
    assert 0 <= Control.STICK_SENSITIVITY <= 10
    assert 1 <= Ship.ACCURACY <= 10
    assert 0 < Ship.RESIST < 1
    assert Ship.SMOOTH >= 1
    assert Meteor.MAX_SIZE >= Meteor.MIN_SIZE
    assert Rocket.SPEED > 0
    assert 0 <= DynamicBG.OPACITY <= 100
    assert 1 <= Sound.Volume.GENERAL <= 10
    assert 1 <= Sound.Volume.CLICK <= 10
    assert 1 <= Sound.Volume.SHOOT <= 10
    assert 1 <= Sound.Volume.BG_GAME <= 10
    assert 1 <= Sound.Volume.BG_MENU <= 10
    assert 1 <= Sound.Volume.EX_METEORS <= 10
    assert 1 <= Sound.Volume.EX_PLAYER <= 10

