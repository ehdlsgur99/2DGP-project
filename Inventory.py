import ObjectManager
import item
import object
import KeyManager
import status

class inventory:
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
        self.items = []
        self.popup = object.obj("Resource/inven.png", 800, 350, 306, 533, 0)


    def update(self):
        for i in self.items:
            i.update()
            if KeyManager.mouseDown == True:
                if KeyManager.mouseXPos > i.image.x - 30 / 2 and KeyManager.mouseXPos < i.image.x + 30 / 2 and KeyManager.mouseYPos > i.image.y - 30 / 2 and KeyManager.mouseYPos < i.image.y + 30 / 2:
                    if i.type != 'Potion' :
                        status.Status.instance().addWeapon(i)
                        self.items.remove(i)
                        KeyManager.mouseDown = False
                    else:
                        ObjectManager.Player.HP += i.potionVal
                        if ObjectManager.Player.HP > 100:
                            ObjectManager.Player.HP = 100
                        self.items.remove(i)


                    return




    def render(self):
        self.popup.drawSize(300, 500)
        count = 0

        for i in self.items:

            i.image.x = i.x = 650 + 75 + (count%3) * 75
            i.image.y = i.y = 500 - int(count/3) * 75
            i.textBox.x = i.image.x - 200
            i.textBox.y = i.image.y

            i.render()
            count += 1
        pass

    def release(self):
        pass

