from components.window import Window


class SpaceBattle:
    def __init__(self):
        self.window = Window()

    def show(self):
        self.window.process()


if __name__ == "__main__":
    game = SpaceBattle()
    game.show()
