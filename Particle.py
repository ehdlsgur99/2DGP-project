from pico2d import *
import object
# 파티클 관리하는 배열 만들고 체크

class Particle():
    def __init__(self):
        self.particles = []

    def addParticles(self,path,frame, x, y, width, height):
        p = object.obj(path, x, y, width, height, frame)
        self.particles.append(p)

    def update(self):
        for p in self.particles:
            if p.animation() == True:
                self.particles.remove(p)

    def render(self):
        for p in self.particles:
            p.image.clip_composite_draw(0, 0, p.width, p.height, 0.0, 'none', p.x, p.y)