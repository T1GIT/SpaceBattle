from collections import deque

import pygame as pg

from config import Configuration as Conf
from managers.image import Image as Img


class Animation(pg.sprite.Sprite):
    """
    """
    skip_frame = Conf.Rules.FPS // Conf.Animation.FPS

    def __init__(self, name: str):
        pg.sprite.Sprite.__init__(self)
        # Texture wearing
        raw_frames = Img.get_animation(name)
        w0, h0 = raw_frames[0].get_size()
        scale = Conf.Animation.SIZE / max(w0, h0)
        w1, h1 = map(lambda x: round(x * scale), [w0, h0])
        self.frames = []
        for frame in raw_frames:
            self.frames.append(pg.transform.scale(frame, (w1, h1)))
        self.frames = deque(self.frames)
        self.image = self.frames.popleft()
        self.skipped = 1

    def locate(self, x, y):
        """
        Shows sprite in the screen
        :param x: position of the end
        :param y: position of the end
        """
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        if self.skipped % self.skip_frame == 0:
            if len(self.frames) > 0:
                self.image = self.frames.popleft()
                self.rect = self.image.get_rect(center=self.rect.center)
            else:
                self.kill()
        self.skipped += 1
