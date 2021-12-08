import item
import object

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

    def render(self):
        self.popup.drawSize(300, 500)
        for i in self.items:
            i.render()
        pass

    def release(self):
        pass

