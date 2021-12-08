import Button
import ObjectManager
import object
from pico2d import *
import KeyManager
import Inventory

ITEM_TYPE = {'Sword' : 'Sword', 'Shield' : 'Shield', 'Potion' : 'Potion'}
ITEM_GRADE = {'Legend' : 'Legend ', 'Unique' : 'Unique ', 'Rare' : 'Rare ', 'Normal' : 'Normal '}

class item:
    def __init__(self, path, type, x, y,  grade, frame = 0, gold = 0 ):
        self.x = x
        self.y = y
        self.grade = grade
        self.type = type
        self.gold = gold
        self.image = object.obj(path, x, y, 1000, 1000, 0)
        self.buyButton = Button.button('resource/item/buyButton1.png', 'resource/item/buyButton2.png', x + 200, y, 1027, 564, 75, 40, frame, self.getNowItem)
        self.font = load_font('ENCR10B.TTF', 16)
        self.name = ITEM_GRADE[self.grade] + ITEM_TYPE[self.type]
        self.power = 0
        self.armor = 0
        self.potionVal = 0
        self.createStatus()
        self.isBuy = False
        # 설명 텍스트 박스 설정
        self.textBox = object.obj('resource/item/textbox.png', x+ 150, y, 1027, 564, 0)
    def createStatus(self):
        if self.grade == 'Legend':
            self.power = 100
            self.armor = 100
            self.potionVal = 100
        elif self.grade == 'Unique':
            self.power = 50
            self.armor = 50
            self.potionVal = 50
        elif self.grade == 'Rare':
            self.power = 30
            self.armor = 30
            self.potionVal = 30
        elif self.grade == 'Normal':
            self.power = 10
            self.armor = 10
            self.potionVal = 10

    def getNowItem(self):
        # 플레이어 인벤토리에 아이템을 추가시켜준다.
        # 그리고 수명을 다했으므로 버튼을 비활성화 시킨다.
        Inventory.inventory.instance().items.append(self)
        ObjectManager.Player.coinNum -= self.gold
        self.isBuy = True
    def update(self):
        if self.isBuy == False:
            self.buyButton.update()


    # 아이템 옆에 얼마 인지도 그려 준다.
    def render(self):
        self.image.drawSize(50, 50)

        if self.isBuy == False:
            self.buyButton.draw()
            self.font.draw(self.x  + 50, self.y, str(self.gold) + ' GOLD', (255, 255, 0))
        if KeyManager.mouseXPos > self.x - 50/2 and KeyManager.mouseXPos <self.x + 50/2 and KeyManager.mouseYPos > self.y - 50/2 and KeyManager.mouseYPos < self.y + 50/2:
            self.textBox.drawSize(200, 100)
            print(self.name)

            if self.isBuy == False:
                self.font.draw(self.x + 80, self.y + 20, self.name, (255, 255, 255))
                if self.type == 'Sword':
                    self.font.draw(self.x + 80, self.y, 'power : ' + str(self.power), (255, 255, 255))
                elif self.type == 'Shield':
                    self.font.draw(self.x + 80, self.y, 'armor : ' + str(self.power), (255, 255, 255))
                elif self.type == 'Potion':
                    self.font.draw(self.x + 80, self.y, 'heal : ' + str(self.power), (255, 255, 255))
            elif self.isBuy == True:
                self.font.draw(self.x - 280, self.y + 20, self.name, (255, 255, 255))
                if self.type == 'Sword':
                    self.font.draw(self.x - 280, self.y, 'power : ' + str(self.power), (255, 255, 255))
                elif self.type == 'Shield':
                    self.font.draw(self.x - 280, self.y, 'armor : ' + str(self.power), (255, 255, 255))
                elif self.type == 'Potion':
                    self.font.draw(self.x - 280, self.y, 'heal : ' + str(self.power), (255, 255, 255))






