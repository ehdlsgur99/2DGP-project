from pico2d import *

class obj():
    def __init__(self, path, x, y, width, height):
        self.image = load_image(path)
        self.x, self.y = x,y
        self.width, self.height = width, height
        self.isVisible = True
    def render(self):
        self.image.clip_composite_draw(0, 0, self.width, self.height, 0.0, 'none', self.x, self.y)
