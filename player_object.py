from pico2d import *


class Player:
    def __init__(self):
        self.image = load_image('player.png')
        self.x, self.y = 100, 100
        self.state = 'idle'
        self.frame = 0
        self.rad = 90.0
    def draw(self):
        self.image.clip_composite_draw(self.frame * 100, 100 * 1, 100, 100, self.rad, 'none', self.x, self.y, 100, 100)

    def update(self):
        self.x = self.x + 1
        self.y = self.y + 1

        #update_animation
        if(Player.frame > 5):
            self.frame = 0


    def update_state(self, moveX = 0, moveY = 0):
        xDirection = self.x - moveX
        yDirection = self.y - moveY
        if xDirection < 0:
            self.state = 'right'
        elif xDirection >0:
            self.state = 'left'
        elif xDirection < 0:
            self.state = 'left'
        elif yDirection > 0:
            self.state = 'down'
        elif yDirection < 0:
            self.state = 'up'