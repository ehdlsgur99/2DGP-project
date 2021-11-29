import object
import Button
from pico2d import *

ITEM_TYPE = {''}

class item():

    def __init__(self, type, path, x, y, width, height, frame = 0, gold = 0 ):
        self.x = x
        self.y = y
        self.type = type
        self.width = width
        self.height = height
        self.gold = gold
        self.obj = Button.button(path+'1.png', path+'2.png', x, y, width, height, frame, self.getNowItem())
        self.font = load_font('ENCR10B.TTF', 16)

    def getNowItem(self):
        return self

    def update(self):
        self.obj.update()

    # 아이템 옆에 얼마 인지도 그려 준다.
    def render(self):
        self.obj.draw()
        self.font.draw(self.x + self.width + 30, self.y, str(self.gold), (255, 255, 0))






