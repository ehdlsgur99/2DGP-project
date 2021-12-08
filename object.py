from pico2d import *

class obj():
    def __init__(self, path, x, y, width, height, frame = 0):
        self.image = load_image(path)
        self.x, self.y = x,y
        self.width = width
        self.height = height
        self.isVisible = True
        self.frame = frame
        self.nowFrame = 0
        self.opacify = 0
    def draw(self):
        self.image.clip_composite_draw(self.nowFrame *self.width , 0, self.width, self.height, 0.0, 'none', self.x, self.y)

    def drawSize(self, width, height):
        self.image.clip_composite_draw(self.nowFrame * self.width, 0, self.width, self.height, 0.0, 'none', self.x,
                                       self.y, width, height)

    def changeOpacity(self, o):
        self.opacify = o
        self.image.opacify(self.opacify)

    def animation(self):
        if self.nowFrame >= self.frame:
            self.nowFrame = 0
            return True
        else:
            self.nowFrame += 1

    def update(self):
        self.animation()

    def getPos(self):
        return self.x, self.y

    def getSize(self):
        return self.width, self.height
