import pygame as pg

from config import Configuration as Conf
from managers.image import Image as Img


class Overlay:
    def __init__(self, window):
        life_image = Img.get_life()
        self.texture = pg.transform.scale(life_image, (Conf.Overlay.Health.SIZE, Conf.Overlay.Health.SIZE))
        self.image = self.texture
        self.font = pg.font.Font('./resources/fonts/opensans.ttf', Conf.Overlay.Score.FONT_SIZE)

        self.window = window
        self.score = 0
        self.life = []

    def get_health(self):
        return len(self.life)

    def get_score(self):
        return self.score

    def add_to_life(self, obj):
        self.life.append(obj)

    def reset(self):
        """
        Zero out all variables
        """
        self.score = 0
        self.life = [0] * Conf.Rules.LIVES

    def up_score(self):
        """
        Raises score in the overlay
        """
        # May request delta in func parameter, or write it into Conf.Overlay
        # TODO: Damir
        self.score += Conf.Overlay.Score.NUMBER

    def down_life(self):
        """
        Subtracts one life
        """
        # TODO: Damir
        if self.life:
            self.life[-1].kill()
            del self.life[-1]
        else:
            pass

    def is_alive(self) -> bool:
        """
        Checks if is it has life
        :return True if it has life
        """
        # TODO: Damir
        if not self.life:
            return False
        else:
            return True

    def show_score(self):
        score = self.font.render(f"{self.get_score()}", True, Conf.Overlay.Score.FONT_COLOR)
        score_rect = score.get_rect()
        score_rect.topright = (Conf.Window.HEIGHT - Conf.Overlay.Score.X_OFFSET, Conf.Overlay.Score.Y_OFFSET)

        self.window.window.screen.blit(score, score_rect)


    class Health(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            life_image = Img.get_life()
            self.texture = pg.transform.scale(life_image, (Conf.Overlay.Health.SIZE, Conf.Overlay.Health.SIZE))
            self.image = self.texture

        def show_health(self, x):
            self.rect = self.image.get_rect(center=(x, Conf.Overlay.Health.Y_OFFSET))
