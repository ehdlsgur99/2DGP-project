import random
import Collision_Manager
from pico2d import *


class GoblinMonster():
    def __init__(self):
        self.image = load_image('Resource/Monster/Goblin/Idle.png')
        self.x, self.y = random.randint(0, 1000), random.randint(0, 700)
        self.frame = 0
        self.directionX = 0.0
        self.directionY = 0.0
        self.speed = 1.0
        self.state = 'idle'
        self.rad = 0
        self.isMove = False
        self.isTarget = False
        self.isVisible = True
        self.HP = 10

    def die(self):
        self.HP = 0
        self.isVisible = False

    def update(self):
        self.animation()
        # 이동
        self.x += self.directionX*0.1
        self.y += self.directionY * 0.1
        pass

    def animation(self):
        # 방향 체크
        if self.directionX > 0:
            if not self.state == 'right':
                self.state = 'right'
                self.image = load_image('Resource/Monster/Goblin/RightMove.png')
        elif self.directionX < 0:
            if not self.state == 'left':
                self.state = 'left'
                self.image = load_image('Resource/Monster/Goblin/LeftMove.png')
        elif self.directionY > 0:
            if not self.state == 'down':
                self.state = 'down'
                self.image = load_image('Resource/Monster/Goblin/DownMove.png')
        elif self.directionY < 0:
            if not self.state == 'up':
                self.state = 'up'
                self.image = load_image('Resource/Monster/Goblin/UpMove.png')
        if self.frame > 3:
            self.frame = 0
        else:
            self.frame = self.frame + 1

    def checkPlayer(self, player):
        if Collision_Manager.CollisionManager.checkCircleCollision(player.x, player.y, self.x, self.y, 100):
            moveXVec = player.x - self.x
            moveYVec = player.y - self.y
            dis = math.sqrt(math.pow(moveXVec, 2)) + math.sqrt(math.pow(moveYVec, 2))
            moveXVec += moveXVec / dis
            moveXVec += moveXVec / dis
            self.directionX = moveXVec
            self.directionY = moveYVec
            self.isTarget = True
        else:
            self.directionX = 0
            self.directionY = 0
            self.isTarget = False
            self.state = 'idle'
            self.image = load_image('Resource/Monster/Goblin/Idle.png')

    def render(self):
        if self.isVisible == False:
            return
        self.image.clip_composite_draw(self.frame * 48, 0, 48, 48, self.rad, 'none', self.x, self.y, 100, 100)
        pass


class zombieMonster():
    def __init__(self):
        self.image = load_image('Resource/Monster/Zombie/Idle.png')
        self.x, self.y = random.randint(0, 1000), random.randint(0, 700)
        self.frame = 0
        self.directionX = 0.0
        self.directionY = 0.0
        self.speed = 1.0
        self.state = 'idle'
        self.rad = 0
        self.isMove = False
        self.isTarget = False
        self.isVisible = True
        self.HP = 10

    def die(self):
        self.HP = 0
        self.isVisible = False

    def update(self):
        self.animation()
        self.x += self.directionX * 0.1
        self.y += self.directionY * 0.1
        # 이동

    def animation(self):
        # 방향 체크
        if self.directionX > 0:
            if not self.state == 'right':
                self.state = 'right'
                self.image = load_image('Resource/Monster/Zombie/RightMove.png')
        elif self.directionX < 0:
            if not self.state == 'left':
                self.state = 'left'
                self.image = load_image('Resource/Monster/Zombie/LeftMove.png')
        elif self.directionY > 0:
            if not self.state == 'down':
                self.state = 'down'
                self.image = load_image('Resource/Monster/Zombie/DownMove.png')
        elif self.directionY < 0:
            if not self.state == 'up':
                self.state = 'up'
                self.image = load_image('Resource/Monster/Zombie/UpMove.png')
        if self.frame > 3:
            self.frame = 0
        else:
            self.frame = self.frame + 1

    def checkPlayer(self, player):
        if Collision_Manager.CollisionManager.checkCircleCollision(player.x, player.y, self.x, self.y, 100):
            moveXVec = player.x - self.x
            moveYVec = player.y - self.y
            dis = math.sqrt(math.pow(moveXVec, 2)) + math.sqrt(math.pow(moveYVec, 2))
            moveXVec += moveXVec / dis
            moveXVec += moveXVec / dis
            self.directionX = moveXVec
            self.directionY = moveYVec
            self.isTarget = True
        else:
            self.directionX = 0
            self.directionY = 0
            self.isTarget = False
            self.state = 'idle'
            self.image = load_image('Resource/Monster/Zombie/Idle.png')

    def render(self):
        if self.isVisible == False:
            return
        self.image.clip_composite_draw(self.frame * 48, 0, 48, 48, self.rad, 'none', self.x, self.y, 100, 100)
        pass


class bossMonster():
    def __init__(self):
        self.image = load_image('Resource/Monster/Boss/Idle.png')
        self.x, self.y = random.randint(0, 1000), random.randint(0, 700)
        self.frame = 0
        self.directionX = 0.0
        self.directionY = 0.0
        self.speed = 1.0
        self.state = 'idle'
        self.rad = 0
        self.isMove = False
        self.isVisible = True
        self.HP = 10
        pass

    def update(self):
        self.animation()
        self.x += self.directionX*0.1
        self.y += self.directionY * 0.1
        pass

    def animation(self):
        if self.directionX > 0:
            if not self.state == 'right':
                self.state = 'right'
                self.image = load_image('Resource/Monster/Zombie/RightMove.png')
        elif self.directionX < 0:
            if not self.state == 'left':
                self.state = 'left'
                self.image = load_image('Resource/Monster/Zombie/LeftMove.png')
        elif self.directionY > 0:
            if not self.state == 'down':
                self.state = 'down'
                self.image = load_image('Resource/Monster/Zombie/DownMove.png')
        elif self.directionY < 0:
            if not self.state == 'up':
                self.state = 'up'
                self.image = load_image('Resource/Monster/Zombie/UpMove.png')
        if self.frame > 3:
            self.frame = 0
        else:
            self.frame = self.frame + 1
        pass

    def render(self):
        if self.isVisible == False:
            return
        self.image.clip_composite_draw(self.frame * 48, 0, 48, 48, self.rad, 'none', self.x, self.y, 100, 100)

        pass
