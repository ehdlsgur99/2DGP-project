import item
import object
import Inventory
from pico2d import *

# 현재 착용 중인 장비
# 스탯 : 힘 , 체력, armor

class Status:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self.popup = object.obj("Resource/inven.png", 300, 350, 306, 733, 0)
        self.sword = None
        self.armor = None
        self.hp = 100
        self.power = 100
        self.guard = 0
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        pass

    def addWeapon(self, item):
        if item.type == 'Sword':
            if self.sword != None:
                Inventory.inventory.instance().items.append(self.sword)
            self.sword = item
            self.sword.image.x = self.sword.x = 450
            self.sword.image.y = self.sword.y = 500
            self.sword.textBox.x = self.sword.image.x - 200
            self.sword.textBox.y = self.sword.image.y
            self.power = 100 + self.sword.power
        elif item.type == 'Shield':
            if self.armor != None:
                Inventory.inventory.instance().items.append(self.armor)
            self.armor = item
            self.armor.image.x = self.armor.x = 450
            self.armor.image.y = self.armor.y = 400
            self.armor.textBox.x = self.armor.image.x - 200
            self.armor.textBox.y = self.armor.image.y
            self.guard = self.armor.armor
            self.hp = 100 + self.armor.armor
            print(self.armor.armor)

    def render(self):
        self.popup.drawSize(500, 500)
        # 현재 착용 중인 검, 방패
        self.font.draw(200, 500, 'Now Sword : ' , (0, 0, 0))
        if self.sword!= None:
            self.sword.render()
        self.font.draw(200, 400, 'Now Armor : ', (0, 0, 0))
        if self.armor!= None:
            self.armor.render()

        # 공격력 , HP,
        self.font.draw(200, 250, 'POWER : ' + str(100) + ' + ' + str(self.power - 100), (0, 0, 0))
        self.font.draw(200, 200, 'HP : ' + str(100) + ' + ' + str(self.guard), (0, 0, 0))

    def release(self):
        pass


