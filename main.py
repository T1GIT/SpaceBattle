# from components.menu import Menu
from components.window import Window


class SpaceBattle:
    def __init__(self):
        self.window = Window()

    def show(self):
        self.window.show_menu()


if __name__ == "__main__":
    game = SpaceBattle()
    game.show()
