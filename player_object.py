from pico2d import *


class Player:
    def __init__(self):
        self.image = load_image('Resource/Player/Idle.png')
        self.x, self.y = 100, 100
        self.state = 'idle'
        self.frame = 0
        self.rad = 0.0
    def draw(self):
        self.image.clip_composite_draw(self.frame * 48, 0, 48, 48, self.rad, 'none', self.x, self.y, 100, 100)

    def update(self):
        #update_animation
        self.frame = self.frame + 1
        print(self.frame)
        if self.state == 'idle':
            if self.frame > 4:
                self.frame = 0
        else:
            if self.frame > 7:
                self.frame = 0



    def update_state(self, moveX = 0, moveY = 0):
        xDirection = self.x - moveX
        yDirection = self.y - moveY
        if xDirection < 0:
            self.state = 'right'
            self.image = load_image('Resource/Player/RightMove.png')
        elif xDirection <0:
            self.state = 'left'
            self.image = load_image('Resource/Player/LeftMove.png')
        elif yDirection > 0:
            self.state = 'down'
            self.image = load_image('Resource/Player/DownMove.png')
        elif yDirection < 0:
            self.state = 'up'
            self.image = load_image('Resource/Player/UpMove.png')