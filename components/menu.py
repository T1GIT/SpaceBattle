import pygame_menu
from config import Configuration as Conf


class Menu:
    def __init__(self, window):
        # Environment
        self.window = window

        # Initialisation
        # TODO: Damir
        font = pygame_menu.font.FONT_8BIT

        my_theme = pygame_menu.themes.Theme(widget_font=font)
        self.menu = pygame_menu.Menu(Conf.Menu.HEIGHT, Conf.Menu.WIDTH, 'Welcome',
                                     theme=my_theme)

        self.menu.add_text_input('Type name: ')
        self.menu.add_button('Play', pygame_menu.events.EXIT)  # TODO: заменить на функцию выполнения и откоментить
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
