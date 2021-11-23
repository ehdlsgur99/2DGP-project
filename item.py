import object

class item():

    def __init__(self, path, x, y, width, height, frame = 0, gold):
        self.gold = gold
        self.obj = object.obj(path, x, y, width, height, frame)


    def update(self):
        self.obj.update()

    # 아이템 옆에 얼마 인지도 그려 준다.
    def render(self):
        self.obj.draw()






