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
        if self.state == 'idle':
            if self.frame > 4:
                self.frame = 0
        else:
            if self.frame > 7:
                self.frame = 0

        if self.state == 'right':
            self.x = self.x + 10
        elif self.state == 'left':
            self.x = self.x - 10
        elif self.state == 'up':
            self.y = self.y + 10
        elif self.state == 'down':
            self.y = self.y - 10



    def update_state(self, direction):
        if self.state == direction:
            return

        if direction == 'right':
            self.state = 'right'
            self.image = load_image('Resource/Player/RightMove.png')
        elif direction == 'left':
            self.state = 'left'
            self.image = load_image('Resource/Player/LeftMove.png')
        elif direction == 'down':
            self.state = 'down'
            self.image = load_image('Resource/Player/DownMove.png')
        elif direction == 'up':
            self.state = 'up'
            self.image = load_image('Resource/Player/UpMove.png')
        elif direction == 'idle':
            self.state = 'idle'
            self.image = load_image('Resource/Player/Idle.png')
