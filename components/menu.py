import pygame_menu

from config import Configuration as Conf
from utils.listener.events import Event, Device as Dvs, Keyboard as Kb, Gamepad as Gp
from utils.resources.image import Image as Img
from utils.listener.listener import EventListener
from utils.resources.sound import Sound as Snd


class Menu:
    def __init__(self, window):
        # Environment
        self.window = window
        self.engine = pygame_menu.sound.Sound()
        self.menu: dict[str, pygame_menu.Menu] = dict()
        self.time = 0

    def create_about(self):
        """
        Create menus: About
        This function contains an about list that displays text on the screen.
        A separate about theme is created by copying the standard one,
        the theme is customized - the font of the title is changed.
        """
        ABOUT = ['Game version: {0}'.format(Conf.Menu.GAME_VERSION),
                 f'Authors: {Conf.Menu.AUTHORS[0]}, {Conf.Menu.AUTHORS[1]}, {Conf.Menu.AUTHORS[2]}',
                 '',
                 'Ideas and suggestions: SpaceBattle@ya.com']

        # Theme
        about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
        about_theme.title_font_size = 56

        # Initialisation
        self.menu["about"] = pygame_menu.Menu(
            height=Conf.Window.HEIGHT,
            width=Conf.Window.WIDTH,
            onclose=pygame_menu.events.DISABLE_CLOSE,  # Action on closing
            theme=about_theme,  # Setting theme
            title='About'
        )

        # Layout
        for m in ABOUT:
            self.menu["about"].add_label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=30)
        self.menu["about"].add_vertical_margin(Conf.Window.WIDTH / 4)
        self.menu["about"].add_button(
            'Return to menu',
            pygame_menu.events.BACK,
            selection_color=(0, 0, 0),
        )

    def create_settings(self):
        """
        Create menus: Settings
        This function contains an about list that displays text on the screen.
        A separate about theme is created by copying the standard one,
        the theme is customized - the font of the title is changed.
        """

        # Theme
        theme = pygame_menu.themes.THEME_SOLARIZED.copy()
        theme.title_font_size = 56

        # Initialisation
        self.menu["settings"] = pygame_menu.Menu(
            height=Conf.Window.HEIGHT,
            width=Conf.Window.WIDTH,
            onclose=pygame_menu.events.DISABLE_CLOSE,  # Action on closing
            theme=theme,  # Setting theme
            title='Settings'
        )

        # Layout
        self.menu["settings"].add_text_input(
            f'General volume: ',
            font_color=(0, 0, 0),
            input_type=pygame_menu.locals.INPUT_FLOAT,
            default=Conf.Sound.Volume.GENERAL,
            maxchar=2,
            onreturn=Snd.Volume.set_general
        )
        self.menu["settings"].add_text_input(
            f'Background music volume: ',
            font_color=(0, 0, 0),
            input_type=pygame_menu.locals.INPUT_FLOAT,
            default=Conf.Sound.Volume.BG,
            maxchar=2,
            onreturn=Snd.Volume.set_bg
        )
        self.menu["settings"].add_text_input(
            f'SFX volume: ',
            font_color=(0, 0, 0),
            input_type=pygame_menu.locals.INPUT_FLOAT,
            default=Conf.Sound.Volume.SFX,
            maxchar=2,
            onreturn=Snd.Volume.set_sfx
        )
        self.menu["settings"].add_vertical_margin(100)
        self.menu["settings"].add_button(
            'Return to menu',
            pygame_menu.events.BACK,
            selection_color=(0, 0, 0),
        )

    def create_menu(self):
        """
        Create menus: Main. Responsible for setting up the main menu.
        A picture is selected for the background. Customizable theme, colors, font size, etc.
        A name entry line is added, a play button that redirects to the start function of the game,
        similarly with the about and exit buttons.
        """

        # Theme
        theme = pygame_menu.themes.Theme(
            selection_color=Conf.Menu.THEME_COLOR,
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,  # Separating header and body
            title_offset=(Conf.Menu.Title.X_OFFSET, Conf.Menu.Title.Y_OFFSET),
            title_font_color=(255, 255, 255),
            title_font_size=Conf.Menu.Title.SIZE,
            background_color=Img.get_menu(),
            widget_font_color=(255, 255, 255),
            widget_font_size=40,
            widget_margin=(0, 40),
            menubar_close_button=False  # Removing the close button
        )

        # Initialisation
        self.menu["main"] = pygame_menu.Menu(
            Conf.Window.HEIGHT,
            Conf.Window.WIDTH,
            title='SPACE BATTLE',
            theme=theme,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            mouse_motion_selection=True
        )

        # Layout
        self.menu["main"].add_button('     Play     ', self.window.start, font_size=60, margin=(0, 50))
        self.menu["main"].add_button('   Settings   ', self.menu["settings"])
        self.menu["main"].add_button('     About     ', self.menu["about"])
        self.menu["main"].add_button('     Quit     ', exit)

        # Sound
        self.engine.set_sound(pygame_menu.sound.SOUND_TYPE_CLICK_MOUSE, Snd.click(),
                              volume=Snd.get_volume(Conf.Sound.Volume.SFX))
        self.menu["main"].set_sound(self.engine, recursive=True)

    def start(self):
        self.window.start()

    def event_handler(self, events: dict[str, set[Event]]):
        for event in events[Dvs.KEYBOARD] | events[Dvs.GAMEPAD]:
            if (event.get_data() == Kb.Keys.ESC
                    or (event.get_type() == Gp.Events.KEY
                        and event.get_data() == Gp.Keys.START)):
                self.window.play()

    def open(self):
        pygame_menu.themes.THEME_DEFAULT.widget_font = pygame_menu.font.FONT_OPEN_SANS  # Setting the default font
        self.create_about()
        self.create_settings()
        self.create_menu()
        self.menu["main"].mainloop(self.window.screen, fps_limit=Conf.System.FPS,
                                   bgfun=lambda: self.event_handler(EventListener.get_events()))

    def close(self):
        self.menu["main"].disable()
