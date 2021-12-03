import item

class store:
    def __init__(self):
        self.items = []
        #  아이템 생성
        self.createItem()

    def createItem(self):
        self.items.append(item.item("sword","sword", 0, 0, 100, 100, 0, 1000))

    def update(self):
        for i in self.items:
            i.update()

    def draw(self):
        for i in self.items:
            i.draw()
