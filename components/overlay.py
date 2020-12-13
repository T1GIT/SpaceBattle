class Overlay:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.life = 3

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
        self.life -= self.life

    def is_alive(self) -> bool:
        """
        Checks if is it has lifes
        :return True if it has lifes
        """
        # TODO: Damir
        if self.life == 0:
            return False
        elif 0 < self.life < 4:
            return True
        else:
            return ArithmeticError
