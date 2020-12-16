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
        FONT = "./resources/fonts/opensans.ttf"

    class Game:
        LOSE_DELAY = 3

    class Overlay:
        OPACITY = 100

        class Score:
            SIZE = 64
            COLOR = (100, 255, 100)
            X_OFFSET = 30
            Y_OFFSET = 5
            DELTA = 300

        class Health:
            SIZE = 50
            MARGIN = 5
            X_OFFSET = 10
            Y_OFFSET = 5

    class Menu:
        GAME_VERSION = "v0.1"
        AUTHORS = "Damir", "Artem", "Dmitriy"
        CONTACTS = ""
        THEME_COLOR = (0, 250, 0)

        class Title:
            X_OFFSET = 100
            Y_OFFSET = 40
            SIZE = 70

    class Piece:
        MIN_OPACITY = 60  # [0, 100]
        MAX_OPACITY = 90  # [0, 100]
        MIN_SIZE = 100  # px
        MAX_SIZE = 300  # px
        MAX_SPEED = 1
        QUANTITY = 10

    class Ship:
        SIZE = 100
        WEIGHT = 2
        POWER = 5
        RESIST = 0.05  # (0; 1)
        SMOOTH = 10  # >= 1
        ACCURACY = 10  # [1; 10]
        DEAD_SPEED = 0.2
        ANIM_SCALE = 3

    class Meteor:
        MAX_SIZE = 100
        MIN_SIZE = 70
        MAX_SPEED = 3
        TOR = True
        ROTATING = True
        MAX_ROTATE_SPEED = 4
        QUANTITY = 20
        BY_TIME = True
        PERIOD = 500
        ON_FIELD = False

    class Rocket:
        SIZE = 10  # px
        SPEED = 20  # > 0
        PERIOD = 200  # ms
        DESTROYABLE = False
        MAX_DISTANCE = 300  # px  (needs Rocket.UNLIMITED = False)
        UNLIMITED = True

    class Animation:
        DEFAULT_SIZE = 200
        FPS = 30

    class Image:
        SHIP = 0
        LIFE = 0
        ROCKET = 1
        MENU_BG = 0
        STATIC_BG = 0
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
            SFX = 3  # [0; 10]

    class Control:
        MOUSE_BUTTONS = 3
        STICK_SENSITIVITY = 2  # [1; 10]
        STICK_DEAD_ZONE = 0.2
        TRIGGER_DEAD_ZONE = 0.5
        ESC_PERIOD = 500  # ms

    class Rules:
        LIFES = 3

    class System:
        FPS = 60
        GAME_SPEED = 60
        SCALE = GAME_SPEED / FPS

    # Checking parameters
    assert 0 <= Control.STICK_SENSITIVITY <= 10
    assert 1 <= Ship.ACCURACY <= 10
    assert 0 < Ship.RESIST < 1
    assert Ship.SMOOTH >= 1
    assert Meteor.MAX_SIZE >= Meteor.MIN_SIZE
    assert Rocket.SPEED > 0
    assert 0 <= Piece.MIN_OPACITY <= 100
    assert 0 <= Piece.MAX_OPACITY <= 100
    assert 1 <= Sound.Volume.GENERAL <= 10
    assert 1 <= Sound.Volume.SFX <= 10
    assert 1 <= Sound.Volume.BG <= 10
