import pygame_menu

from config import Configuration as Conf
from managers.image import Image as Img


class Menu:
    def __init__(self, window):
        # Environment
        self.window = window

        # Initialisation
        # TODO: Damir
        pygame_menu.themes.THEME_DEFAULT.widget_font = pygame_menu.font.FONT_OPEN_SANS  # Setting the default font
        self.create_about()  # Create the about menu
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
        self.about_menu.add_label('')
        self.about_menu.add_button(
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

        # TODO : добавить в менеджер картинок
        myimage = Img.get_menu()

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

        self.menu.add_text_input('Type name: ')
        self.menu.add_button('Play', self.window.start)
        self.menu.add_button('About', self.about_menu)
        self.menu.add_button('Quit', self.window.exit)

    def show(self):
        """
        Shows menu
        """
        try:
            self.menu.mainloop(self.window.screen, fps_limit=Conf.Rules.FPS)
        except SystemExit:
            self.window.exit()

    def hide(self):
        """
        Hides menu from the window
        """
        self.menu.disable()
