from pico2d import *
import time

class IntroScene():
    def __init__(self):
        self.credit = load_image('Resource/kpu_credit.png')
        self.changeScene = 'none'
        self.startTime = time.time()
        self.rad = 0
        pass

    def update(self):
        if time.time() - self.startTime > 1.0:
            self.changeScene = 'VillageScene'
        return self.changeScene

    def render(self):
        self.credit.clip_composite_draw(0, 0, 800, 600, self.rad, 'none', 500, 350, 1000, 700)
        pass

    def release(self):
        pass
