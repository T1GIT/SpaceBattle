import pygame as pg
import pygame_menu

from config import Configuration as Conf
from managers.image import Image as Img
from managers.sound import Sound


class Menu:
    def __init__(self, window):
        # Environment
        self.window = window

        # Initialisation
        # TODO: Damir
        self.engine = pygame_menu.sound.Sound()
        self.engine.set_sound(pygame_menu.sound.SOUND_TYPE_CLICK_MOUSE,
                              "./resources/sounds/menu/Click.mp3",
                              volume=Conf.Sounds.CLICK)
        self.mng_sound = Sound()
        self.mng_sound.menu_music()
        pygame_menu.themes.THEME_DEFAULT.widget_font = pygame_menu.font.FONT_OPEN_SANS  # Setting the default font
        self.create_about()  # Create the about menu
        self.create_settings()
        self.create_menu()  # Create the main menu

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

        about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
        about_theme.title_font_size = 56

        self.about_menu = pygame_menu.Menu(
            height=Conf.Window.HEIGHT,
            width=Conf.Window.WIDTH,
            onclose=pygame_menu.events.DISABLE_CLOSE,  # Action on closing
            theme=about_theme,  # Setting theme
            title='About'
        )

        for m in ABOUT:
            self.about_menu.add_label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=30)
        self.about_menu.add_vertical_margin(Conf.Window.WIDTH / 4)
        self.about_menu.add_button(
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

        settings_theme = pygame_menu.themes.THEME_DEFAULT.copy()
        settings_theme.title_font_size = 56

        self.settings_menu = pygame_menu.Menu(
            columns=2,
            rows=4,
            height=Conf.Window.HEIGHT,
            width=Conf.Window.WIDTH,
            onclose=pygame_menu.events.DISABLE_CLOSE,  # Action on closing
            theme=settings_theme,  # Setting theme
            title='Settings'
        )

        # TODO: в другое место
        def change_general_sound(value):
            Conf.Sounds.GENERAL = value/100

        def change_game_sound(value):
            Conf.Sounds.BACKGROUND_GAME = value/100

        def change_menu_sound(value):
            Conf.Sounds.BACKGROUND_MENU = value/100
            self.mng_sound.menu_music()

        def change_fire_sound(value):
            Conf.Sounds.FIRE = value / 100

        self.settings_menu.add_text_input(
            f'General sound: ',
            font_color=(0, 0, 0),
            input_type=pygame_menu.locals.INPUT_FLOAT,
            default=round(Conf.Sounds.GENERAL * 100),
            maxchar=3,
            onreturn=change_general_sound
        )

        self.settings_menu.add_text_input(
            f'Game music: ',
            font_color=(0, 0, 0),
            input_type=pygame_menu.locals.INPUT_FLOAT,
            default=round(Conf.Sounds.BACKGROUND_GAME * 100),
            maxchar=3,
            onreturn=change_game_sound
        )

        self.settings_menu.add_text_input(
            f'Menu music: ',
            font_color=(0, 0, 0),
            input_type=pygame_menu.locals.INPUT_FLOAT,
            default=round(Conf.Sounds.BACKGROUND_MENU * 100),
            maxchar=3,
            onreturn=change_menu_sound
        )

        self.settings_menu.add_text_input(
            f'Fire sound : ',
            font_color=(0, 0, 0),
            input_type=pygame_menu.locals.INPUT_FLOAT,
            default=round(Conf.Sounds.FIRE * 100),
            maxchar=3,
            onreturn=change_fire_sound
        )

        self.settings_menu.add_vertical_margin(100)
        self.settings_menu.add_button(
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

        myimage = Img.get_menu()

        def change_name(name):
            pass

        my_theme = pygame_menu.themes.Theme(
            selection_color=(0, 250, 0),
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,  # Separating header and body
            title_offset=(Conf.Menu.Title.X_OFFSET, Conf.Menu.Title.Y_OFFSET),
            title_font_color=(255, 255, 255),
            title_font_size=Conf.Menu.Title.SIZE,
            background_color=myimage,
            widget_font_color=(255, 255, 255),
            widget_font_size=40,
            widget_margin=(0, 40),
            menubar_close_button=False  # Removing the close button
        )

        self.menu = pygame_menu.Menu(
            Conf.Window.HEIGHT,
            Conf.Window.WIDTH,
            title='SPACE BATTLE',
            theme=my_theme,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            mouse_motion_selection=True
        )
        self.menu.set_sound(self.engine, recursive=True)

        self.menu.add_text_input('Type name: ', onchange=change_name)
        self.menu.add_button('Play', self.window.process)
        self.menu.add_button('Settings', self.settings_menu)
        self.menu.add_button('About', self.about_menu)
        self.menu.add_button('Quit', self.window.exit)

    def exit(self):
        self.menu.disable()

    def show(self):
        """
        Shows menu
        """
        # TODO: Damir
        self.menu.mainloop(self.window.screen)

    def hide(self):
        """
        Hides menu from the window
        """
        # TODO: Damir
