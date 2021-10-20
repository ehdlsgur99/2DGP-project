from pico2d import *
import CollisionManager

class Player:
    def __init__(self):
        self.image = load_image('Resource/Player/Idle.png')
        self.moveDirection = [False, False, False, False] # r-l-u-d
        self.x, self.y = 100, 100
        self.state = 'idle'
        self.frame = 0
        self.rad = 0.0
        self.prevState = 'idle'
        self.isAttack = False
        self.CM = CollisionManager.CM()
    def draw(self):
        self.image.clip_composite_draw(self.frame * 48, 0, 48, 48, self.rad, 'none', self.x, self.y, 100, 100)
    def checkMonster(self, monsters):
        if self.isAttack:
            for m in monsters:
                if self.CM.checkCircleCollisionCheck(m.x, m.y, self.x, self.y, 30) and m.isVisible == True:
                    print(self.isAttack)
                    m.die()



    def update(self, objects):

        #update_animation
        self.frame = self.frame + 1
        if self.isAttack == True:
            if self.frame > 5:
                self.frame = 0
                self.state = 'idle'
                self.image = load_image('Resource/Player/Idle.png')
                self.moveDirection[0] = False
                self.moveDirection[1] = False
                self.moveDirection[2] = False
                self.moveDirection[3] = False
                self.isAttack = False
        elif self.state == 'idle':
            if self.frame > 4:
                self.frame = 0
        else:
            if self.frame > 7:
                self.frame = 0
        if self.isAttack:
            return

        if self.moveDirection[0] == True:
            self.x = self.x + 10
            for obj in objects:
                if self.CM.checkCircleCollisionCheck(self.x, self.y, obj.x,obj.y, 30 ):
                    self.x = self.x - 10
        if self.moveDirection[1] == True:
            self.x = self.x - 10
            for obj in objects:
                if self.CM.checkCircleCollisionCheck(self.x, self.y, obj.x, obj.y, 30):
                    self.x = self.x + 10
        if self.moveDirection[2] == True:
            self.y = self.y + 10
            for obj in objects:
                if self.CM.checkCircleCollisionCheck(self.x, self.y, obj.x, obj.y, 30):
                    self.y = self.y - 10
        if self.moveDirection[3] == True:
            self.y = self.y - 10
            for obj in objects:
                if self.CM.checkCircleCollisionCheck(self.x, self.y, obj.x, obj.y, 30):
                    self.y = self.y + 10

    def update_state(self, direction):
        if direction == 'attack' and self.isAttack == False:
            self.isAttack = True
            self.frame = 0
            if self.state == 'left':
                self.image = load_image('Resource/Player/WarriorLeftAttack01.png')
            elif self.state == 'right':
                self.image = load_image('Resource/Player/WarriorRightAttack01.png')
            elif self.state == 'up':
                self.image = load_image('Resource/Player/WarriorUpAttack01.png')
            elif self.state == 'down':
                self.image = load_image('Resource/Player/WarriorDownAttack01.png')
            elif self.state == 'idle':
                self.image = load_image('Resource/Player/WarriorDownAttack01.png')
        if self.isAttack== True:
            return

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
