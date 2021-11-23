import object
from pico2d import *

class item():

    def __init__(self, path, x, y, width, height, frame = 0, gold):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gold = gold
        self.obj = object.obj(path, x, y, width, height, frame)
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        self.obj.update()

    # 아이템 옆에 얼마 인지도 그려 준다.
    def render(self):
        self.obj.draw()
        self.font.draw(self.x + self.width + 30, self.y, str(self.gold), (255, 255, 0))






