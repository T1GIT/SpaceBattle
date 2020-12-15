import pygame as pg


class Overlay:
    def __init__(self, window):
        self.window = window
        self.score = 0
        # self.life = 3
        self.life = [0, 0, 0]
        self.health_img = pg.image.load('./resources/images/overlay/health.png')  # TODO: add to managers
        self.health_img = pg.transform.scale(self.health_img, (90, 90))

    def reset(self):
        """
        Zero out all variables
        """
        # TODO: Damir
        self.score = 0
        self.life = 3

    def up_score(self, number):
        """
        Raises score in the overlay
        """
        # May request delta in func parameter, or write it into Conf.Overlay
        # TODO: Damir
        self.score += number

    def down_life(self):
        """
        Subtracts one life
        """
        # TODO: Damir
        if self.life:
            del self.life[-1]
        else:
            ArithmeticError

    def is_alive(self) -> bool:
        """
        Checks if is it has lifes
        :return True if it has lifes
        """
        # TODO: Damir
        if not self.life:
            return False
        else:
            return True

    def show_score(self):
        f1 = pg.font.Font(None, 84)
        text1 = f1.render(f"{self.score}", True,
                          (60, 255, 60))
        self.window.screen.blit(text1, (1650, 60))

    def show_lifes(self):
        show = 0
        x = 20
        while show != len(self.life):
            self.window.screen.blit(self.health_img, (x, 20))
            x += 90
            show += 1
