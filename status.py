import item
import object
import Inventory

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
        self.popup = object.obj("Resource/inven.png", 800, 350, 306, 533, 0)
        self.sword = None
        self.armor = None

    def update(self):
        for i in self.items:
            i.update()

    def addWeapon(self, item):
        if item.type == 'Sword':
            if self.sword != None:
                Inventory.inventory.instance().items.append(self.sword)
            self.sword = item
        elif item.type == 'Shield':
            if self.armor != None:
                Inventory.inventory.instance().items.append(self.armor)
            self.armor = item
        pass

    def render(self):
        self.popup.drawSize(300, 500)
        for i in self.items:
            i.render()
        pass

    def release(self):
        pass

