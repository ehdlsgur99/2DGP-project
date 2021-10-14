from pico2d import *


class Player:
    def __init__(self):
        self.image = load_image('player.png')
        self.x, self.y = 100, 100
    def draw(self):
        self.image.draw(0, 0)

    def update(self):
        self.x = self.x + 1
        self.y = self.y + 1