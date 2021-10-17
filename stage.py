from pico2d import *
import random

class Stage:
    def __init__(self):
        self.width, self.height = 31, 21
        self.map =[[0] for i in range(self.height * self.width)]
        self.grassImage = [load_image('Resource/Stage/grass1.png'),
                             load_image('Resource/Stage/grass2.png'),
                             load_image('Resource/Stage/grass3.png'),
                             load_image('Resource/Stage/grass4.png'),
                             load_image('Resource/Stage/grass5.png'),
                             load_image('Resource/Stage/grass6.png')]

    def draw(self):
        w, h =0, 0
        for i in self.map:
            print(w*3.2, h*32)
            r = random.randint(5)
            self.grassImage[r].clip_composite_draw(0, 0, 32, 32, 0.0, 'none', w * 32, 640 - (h * 32), 32, 32)
            w = w + 1
            if w>30:
                h = h + 1
                w = 0
