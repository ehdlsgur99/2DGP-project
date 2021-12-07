import Button
import object
from pico2d import *

ITEM_TYPE = {''}

class item:
    def __init__(self, type, path, x, y,  grade, frame = 0, gold = 0 ):
        self.x = x
        self.y = y
        self.grade = grade
        self.type = type
        self.gold = gold
        self.image = object.obj(path, x, y, 1027, 564, 0)
        self.buyButton = Button.button('buyButton1.png', 'buyButton1.png', x + 200, y, 1027, 564, frame, self.getNowItem())
        self.font = load_font('ENCR10B.TTF', 16)

    def getNowItem(self):
        return self

    def update(self):
        self.buyButton.update()

    # 아이템 옆에 얼마 인지도 그려 준다.
    def render(self):
        self.image.draw()
        self.buyButton.draw()
        self.font.draw(self.x  + 30, self.y, str(self.gold), (255, 255, 0))






