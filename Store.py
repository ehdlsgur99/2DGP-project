import item

class store:
    def __init__(self):
        self.items = []
        #  아이템 생성
        # self.createItem()
        self.createItem()

    def createItem(self):
        self.items.append(item.item("Resource/item/sword.png", "Sword", 200, 500, 'Unique', 0, 600))
        self.items.append(item.item("Resource/item/shield.png", "Shield", 200, 425, 'Legend', 0, 1000))
        self.items.append(item.item("Resource/item/potion.png", "Potion", 200, 350, 'Normal', 0, 100))

    def update(self):
        for i in self.items:
            i.update()

    def draw(self):
        for i in self.items:
            i.render()
