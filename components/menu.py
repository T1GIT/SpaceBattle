import pygame as pg
import pygame_menu

from config import Configuration as Conf


class Menu:
    def __init__(self, window):
        # Environment
        self.window = window

        # Initialisation
        # TODO: Damir
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
        about_theme.widget_margin = (0, 0)
        about_theme.widget_offset = (0, 0.05)
        about_theme.title_font_size = 56

        self.about_menu = pygame_menu.Menu(
            height=Conf.Menu.HEIGHT,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            theme=about_theme,
            title='About',
            width=Conf.Menu.WIDTH
        )
        for m in ABOUT:
            self.about_menu.add_label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=30)
        self.about_menu.add_label('')
        self.about_menu.add_button('Return to menu', pygame_menu.events.BACK, selection_color=(0, 0, 0), offset=(0, 300))

    def create_menu(self):
        """
        Create menus: Main
        """

        # TODO : добавить в менеджер картинок
        myimage = pygame_menu.baseimage.BaseImage(
            image_path="./resources/textures/menu_bg.jpg",
        )

        my_theme = pygame_menu.themes.Theme(
            selection_color=(0, 250, 0),
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
            title_offset=(Conf.Window.WIDTH/5, 0),
            title_font_color=(255, 255, 255),
            title_font_size=64,
            background_color=myimage,
            widget_font_color=(255, 255, 255),
            widget_font_size=40,
            widget_margin=(0, 40),
            menubar_close_button=False
        )

        self.menu = pygame_menu.Menu(
            Conf.Menu.HEIGHT,
            Conf.Menu.WIDTH,
            title='SPACE BATTLE',
            theme=my_theme,
            onclose=pygame_menu.events.DISABLE_CLOSE,
            mouse_motion_selection=True
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
