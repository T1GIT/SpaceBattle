

class Overlay:
    def __init__(self, game):
        self.game = game
        self.score = 0
        # self.life = 3
        self.life = [0, 0, 0]

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

    # def show_lifes(self):

