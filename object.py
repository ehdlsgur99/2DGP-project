from pico2d import *

class obj():
    def __init__(self, path, x, y, width, height, frame = 0):
        self.image = load_image(path)
        self.x, self.y = x,y
        self.width, self.height = width, height
        self.isVisible = True
        self.frame = frame
        self.nowFrame = 0
    def render(self):
        self.image.clip_composite_draw(0, 0, self.width, self.height, 0.0, 'none', self.x, self.y)

    def animation(self):
        if self.nowFrame >= self.frame:
            self.frame = 0
            return True
        else:
            self.frame += 1

    def update(self):
        self.animation()

    def getPos(self):
        return self.x, self.y

    def getSize(self):
        return self.width, self.height
