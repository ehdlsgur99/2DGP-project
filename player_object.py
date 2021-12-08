import time

from pico2d import *
import Collision_Manager
import KeyManager
import object
import Inventory

class Smash(object.obj):
    def __init__(self, path, x, y, width, height, xDirection, yDirection, xSize, ySize):
        super().__init__(path, x, y, width, height, 0)
        self.xDir, self.yDir = xDirection, yDirection
        self.xSize, self.ySize = xSize, ySize

    def draw(self):
        if self.xDir == 1 and self.yDir ==1:
            self.image.clip_composite_draw(0, 0, self.width, self.height, math.radians(-45), 'none', self.x, self.y,
                                           self.xSize, self.ySize)
        elif self.xDir == 1 and self.yDir ==-1:
            self.image.clip_composite_draw(0, 0, self.width, self.height, math.radians(-135), 'none', self.x, self.y,
                                           self.xSize, self.ySize)
        elif self.xDir == -1 and self.yDir ==1:
            self.image.clip_composite_draw(0, 0, self.width, self.height, math.radians(45), 'none', self.x, self.y,
                                           self.xSize, self.ySize)
        elif self.xDir == -1 and self.yDir == -1:
            self.image.clip_composite_draw(0, 0, self.width, self.height, math.radians(135), 'none', self.x, self.y,
                                           self.xSize, self.ySize)
        elif self.yDir == -1:
            self.image.clip_composite_draw(0, 0, self.width, self.height, math.radians(180), 'none', self.x, self.y, self.xSize, self.ySize)
        elif self.yDir == 1:
            self.image.clip_composite_draw(0, 0, self.width, self.height, 0.0, 'none', self.x, self.y, self.xSize,
                                           self.ySize)
        elif self.xDir == -1:
            self.image.clip_composite_draw(0, 0, self.width, self.height, math.radians(90), 'none', self.x, self.y, self.xSize,
                                           self.ySize)
        elif self.xDir == 1:
            self.image.clip_composite_draw(0, 0, self.width, self.height, math.radians(-90), 'none', self.x, self.y, self.xSize,
                                           self.ySize)

    def update(self):
        self.x += self.xDir * 20
        self.y += self.yDir * 20
        pass

class Player:
    def __init__(self):
        self.image = load_image('Resource/Player/Idle.png')
        self.hpBar = load_image('Resource/hpbar.png')
        self.heart = load_image('Resource/heart.png')
        self.coins = object.obj('Resource/coin.png', 700, 650, 8, 8, 0)
        self.coinNum = 0
        self.moveDirection = [False, False, False, False] # r-l-u-d
        self.x, self.y = 300, 300
        self.state = 'idle'
        self.frame = 0
        self.rad = 0.0
        self.prevState = 'idle'
        self.isAttack = False
        self.isSmash = False
        self.isDash = False
        self.dashTime = 0.0
        self.dashSpeed = 1.0
        self.smashList = []
        self.HP = 100
        self.font = load_font('ENCR10B.TTF', 16)


    def draw(self):
        for i in self.smashList:
            i.draw()
        self.image.clip_composite_draw(self.frame * 48, 0, 48, 48, self.rad, 'none', self.x, self.y, 100, 100)
        self.heart.draw(50, 650, 100, 100)
        self.hpBar.draw(180, 655, self.HP/100 * 200, 20)
        self.coins.drawSize(40, 40)
        self.font.draw(750, 650, str(self.coinNum),(255, 255, 0))

    def attacked(self, damage):
        self.HP -= damage
    def smash(self):
        xDirection = 0
        yDirection = 0
        if KeyManager.now_key_state['RIGHT'] == True:
            xDirection = 1
        if KeyManager.now_key_state['LEFT'] == True:
            xDirection = -1
        if KeyManager.now_key_state['UP'] == True:
            yDirection = 1
        if KeyManager.now_key_state['DOWN'] == True:
            yDirection = -1

        if self.state == 'idle':
            yDirection = -1

        self.update_state('attack')

        smash = Smash('Resource/Player/smash.png', self.x + (xDirection*20), self.y + (yDirection*20), 260, 260,
                        xDirection, yDirection, 80, 50)
        self.smashList.append(smash)


    def checkMonster(self, monsters):
        if self.isAttack:
            for m in monsters:
                if Collision_Manager.CollisionManager.checkCircleCollision(m.x, m.y, self.x, self.y, 30) and m.isVisible == True:
                    m.HP -= 5
                    if m.HP<=0:
                        m.die()
                    self.coinNum += m.coin

    def update(self, objects):

        # smash 업데이트
        for i in self.smashList:
            i.update()
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

        self.coins.update()


        # dash 끝난지 확인
        if self.isDash == True :
            if time.time() - self.dashTime > 0.1:
                self.isDash = False
                self.dashSpeed = 1.0

        # r-l-u-d
        #     아무키도 클릭 x
        moveCount = 0
        if KeyManager.now_key_state['RIGHT'] == True:
            moveCount += 1
            self.x = (self.x + 10) + self.dashSpeed
            for obj in objects:
                if Collision_Manager.CollisionManager.checkCircleCollision(self.x, self.y, obj.x,obj.y, 30 ):
                    self.x = self.x - 10
            if self.state != 'right':
                self.update_state('right')
        if KeyManager.now_key_state['LEFT'] == True:
            moveCount += 1
            self.x = (self.x - 10)  - self.dashSpeed
            for obj in objects:
                if Collision_Manager.CollisionManager.checkCircleCollision(self.x, self.y, obj.x, obj.y, 30):
                    self.x = self.x + 10
            if self.state != 'left':
                self.update_state('left')
        if KeyManager.now_key_state['UP'] == True:
            moveCount += 1
            self.y = (self.y + 10) + self.dashSpeed
            for obj in objects:
                if Collision_Manager.CollisionManager.checkCircleCollision(self.x, self.y, obj.x, obj.y, 30):
                    self.y = self.y - 10
            if self.state != 'up':
                self.update_state('up')
        if KeyManager.now_key_state['DOWN'] == True:
            moveCount += 1
            self.y = (self.y - 10) - self.dashSpeed
            for obj in objects:
                if Collision_Manager.CollisionManager.checkCircleCollision(self.x, self.y, obj.x, obj.y, 30):
                    self.y = self.y + 10
            if self.state != 'down':
                self.update_state('down')
        if moveCount == 0:
            self.update_state('idle')

        if KeyManager.now_key_state['ATTACK'] == True:
            if self.state != 'attack':
                self.update_state('attack')

        if KeyManager.now_key_state['DASH'] == True:
            if self.isDash != 'dash':
                self.update_state('dash')

        if KeyManager.now_key_state['SMASH'] == True:
            if self.state != 'smash':
                self.smash()


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

        if direction == 'dash' and self.isDash == False:
            self.isDash = True
            self.dashSpeed = 20
            self.dashTime = time.time()

