from pico2d import *

class monster_base:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('')
        self.frame = 0
        self.directionX = 0.0
        self.directionY = 0.0
        self.speed = 1.0
        self.state = 'idle'

    def animation(self):
        # 방향 체크
        if self.directionX > 0:
            if not self.state == 'right':
                self.state = 'right'
        elif self.directionX < 0:
            if not self.state == 'left':
                self.state = 'right'
        elif self.directionY > 0:
            if not self.state == 'down':
                self.state = 'down'
        elif self.directionY < 0:
            if not self.state == 'up':
                self.state = 'up'
        if self.frame > 5:
            self.frame = 0
        else:
            self.frame = self.frame + 1



class testMonster(monster_base):
    def __init__(self, strName):
        self.image = load_image(strName)
        pass

