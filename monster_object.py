import random
import time

import ObjectManager
import Collision_Manager
from pico2d import *

import object

class GoblinMonster():
    def __init__(self):
        self.image = load_image('Resource/Monster/Goblin/Idle.png')
        self.hpBar = load_image('Resource/hpbar.png')
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
        self.coin = random.randint(50, 100)

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
        self.hpBar.draw(self.x, self.y + 30, self.HP / 10 * 80, 10)
        pass


class zombieMonster():
    def __init__(self):
        self.image = load_image('Resource/Monster/Zombie/Idle.png')
        self.hpBar = load_image('Resource/hpbar.png')
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
        self.coin = random.randint(50, 100)

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
        self.hpBar.draw(self.x, self.y + 30, self.HP / 10 * 80, 10)
        pass

BOSS_SKILL_TIME = 3

class bossMonster():
    def __init__(self):
        self.image = load_image('Resource/Monster/Boss/idle.png')
        self.hpBar = load_image('Resource/hpbar.png')
        self.x, self.y = 500, 350
        self.frame = 0
        self.directionX = 0.0
        self.directionY = 0.0
        self.speed = 1.0
        self.state = 'idle'
        self.rad = 0
        self.isMove = False
        self.isVisible = True
        self.HP = 10
        self.meteors = []
        self.opacify = 255
        self.skillTime = time.time()
        self.isSkill = False
        self.coin= 1000
        pass

    def die(self):
        self.HP = 0
        self.isVisible = False

    def update(self):
        self.animation()
        self.x += self.directionX*0.1
        self.y += self.directionY * 0.1

        if time.time()  - self.skillTime > BOSS_SKILL_TIME and self.isSkill == False:
            self.isSkill = True
            attackVal = random.randint(0, 0)
            if attackVal == 0:
                self.setMeteor()

    #     meteor attack 상태일때
        if self.state == 'meteorAttack':
            for i in self.meteors:
                self.opacify -= 1
                i.changeOpacity(self.opacify)

            if self.opacify < 0:

                self.opacify = 255
                self.skillTime = time.time()
                self.isSkill = False

                for i in self.meteors:
                    print(i.x, i.y, ObjectManager.Player.x, ObjectManager.Player.y)
                    if Collision_Manager.CollisionManager.checkCircleCollision(i.x, i.y, ObjectManager.Player.x,ObjectManager.Player.y, 100 ) == True:
                        ObjectManager.Player.attacked(10)

                self.meteors.clear()

                #플레이어와 충돌 체크


    def setMeteor(self):
        self.frame = 0
        self.state = 'meteorAttack'
        cnt = random.randint(3, 10)
        for i in range(0, cnt):
            o = object.obj('Resource/Monster/Boss/meteorrange.png', random.randint(100, 900),random.randint(100, 600),
                                           100, 50)
            o.changeOpacity(0)
            self.meteors.append(o)


    def animation(self):
        if self.state != 'meteorAttack':
            if self.directionX > 0:
                if not self.state == 'right':
                    self.state = 'right'
                    self.image = load_image('Resource/Monster/Boss/idle.png')
            elif self.directionX < 0:
                if not self.state == 'left':
                    self.state = 'left'
                    self.image = load_image('Resource/Monster/Boss/idle.png')
            elif self.directionY > 0:
                if not self.state == 'down':
                    self.state = 'down'
                    self.image = load_image('Resource/Monster/Boss/idle.png')
            elif self.directionY < 0:
                if not self.state == 'up':
                    self.state = 'up'
                    self.image = load_image('Resource/Monster/Boss/idle.png')
            if self.state == 'rangeAttack1':
                pass
            elif self.state == 'rageAttack2':
                pass
            elif self.state == 'meteorAttack':
                pass

        if self.frame > 8:
            self.frame = 0
        else:
            self.frame = self.frame + 1

    def render(self):
        if self.isVisible == False:
            return
        if self.directionX >0:
            self.image.clip_composite_draw(self.frame * 100, 0, 100, 100, self.rad, 'none', self.x, self.y, 400, 400)
        else:
            self.image.clip_composite_draw(self.frame * 100, 0, 100, 100, self.rad, 'h', self.x, self.y, 400, 400)
        self.hpBar.draw(self.x, self.y + 110, self.HP / 10 * 200, 10)


    #     meteor 출력
        if self.state == 'meteorAttack':
            for i in self.meteors:
                i.draw()

    def checkPlayer(self, player):
        if self.isSkill == True:
            return
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
            self.image = load_image('Resource/Monster/Boss/idle.png')
