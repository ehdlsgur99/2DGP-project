import object
import item

class Store:
    def __init__(self):
        self.items = []
        pass

    #  아이템 생성
    def createItem(self):
        pass

    def update(self):
        for i in self.items:
            i.update()

    def render(self):
        for i in self.items:
            i.update()
        pass
