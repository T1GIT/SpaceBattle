import pygame
import pygame_menu
import os.path as path
from config import Configuration as Conf


class Menu:
    def __init__(self, window):
        # Environment
        self.window = window

        # Initialisation
        # TODO: Damir
        # self.font = pygame_menu.font.FONT_OPEN_SANS
        pygame_menu.themes.THEME_DEFAULT.widget_font = pygame_menu.font.FONT_OPEN_SANS
        self.create_about()
        self.create_menu()

    def create_about(self):
        """
        Create menus: About
        """
        ABOUT = ['Game version: {0}'.format(Conf.Menu.GAME_VERSION),
                 f'Authors: {Conf.Menu.AUTHORS[0]}, {Conf.Menu.AUTHORS[1]}, {Conf.Menu.AUTHORS[2]}',
                 '',
                 'Ideas and suggestions: SpaceBattle@ya.com']

        about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
        # about_theme.widget_font = self.font
        about_theme.widget_margin = (0, 0)
        about_theme.widget_offset = (0, 0.05)

        self.about_menu = pygame_menu.Menu(
            height=Conf.Menu.HEIGHT,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            theme=about_theme,
            title='About',
            width=Conf.Menu.WIDTH,
        )
        for m in ABOUT:
            self.about_menu.add_label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
        self.about_menu.add_label('')
        self.about_menu.add_button('Return to menu', pygame_menu.events.BACK)

    def create_menu(self):
        """
        Create menus: Main
        """

        my_theme = pygame_menu.themes.Theme()
        self.menu = pygame_menu.Menu(
            Conf.Menu.HEIGHT,
            Conf.Menu.WIDTH,
            'SPACE BATTLE',
            theme=my_theme,
            onclose=pygame_menu.events.DISABLE_CLOSE
        )

        self.menu.add_text_input('Type name: ')
        self.menu.add_button('Play', self.window.start)
        self.menu.add_button('About', self.about_menu)
        self.menu.add_button('Quit', pygame_menu.events.EXIT)

    def reset(self):
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
