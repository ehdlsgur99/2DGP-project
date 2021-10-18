from pico2d import *


class Player:
    def __init__(self):
        self.image = load_image('Resource/Player/Idle.png')
        self.moveDirection = [False, False, False, False] # r-l-u-d
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

        if self.moveDirection[0] == True:
            self.x = self.x + 10
        if self.moveDirection[1] == True:
            self.x = self.x - 10
        if self.moveDirection[2] == True:
            self.y = self.y + 10
        if self.moveDirection[3] == True:
            self.y = self.y - 10



    def update_state(self, direction):

        if direction == 'right':
            self.state = 'right'
            if self.moveDirection[0] == False:
                self.image = load_image('Resource/Player/RightMove.png')
            self.moveDirection[0] = not self.moveDirection[0]

        elif direction == 'left':
            self.state = 'left'
            if self.moveDirection[1] == False:
                self.image = load_image('Resource/Player/LeftMove.png')
            self.moveDirection[1] = not self.moveDirection[1]
        elif direction == 'down':
            self.state = 'down'
            if self.moveDirection[3] == False:
                self.image = load_image('Resource/Player/DownMove.png')
            self.moveDirection[3] = not self.moveDirection[3]
        elif direction == 'up':
            self.state = 'up'
            if self.moveDirection[2] == False:
                self.image = load_image('Resource/Player/UpMove.png')
            self.moveDirection[2] = not self.moveDirection[2]


        count = 0
        for i in self.moveDirection:
            if i == True:
                count = count + 1
        if count == 0:
            self.state = 'idle'
            self.image = load_image('Resource/Player/Idle.png')
