from pico2d import *
import player_object
import Collision_Manager
import object
import time
import KeyManager

class VillageScene():
    def __init__(self):

        self.bg = load_image('Resource/Stage/map.png')
        self.player = player_object.Player()
        print(self.player.state)
        self.changeScene = 'none'
        self.begin = time.time()

        self.portal = load_image('Resource/Stage/portal.png')

        self.objects = []
        self.objects.append(object.obj('Resource/Stage/aaa.png', 100, 350, 1000, 700))
        self.objects.append(object.obj('Resource/Stage/aaa.png', 300, 350, 1000, 700))
    def update(self):
        KeyManager.handle_events()
        self.player.update(self.objects)

        # 포탈에 들어갔다면?

        if Collision_Manager.CollisionManager.checkCircleCollision(self.player.x, self.player.y, 500, 100, 100):
            self.changeScene = 'DungeonScene'
        return self.changeScene

    def render(self):

        self.bg.clip_composite_draw(0, 0, 1000, 700, 0.0, 'none', 500, 350)

        for i in self.objects:
            i.draw()
        # 포탈 출력
        self.portal.clip_composite_draw(0, 0, 100, 100, 0.0, 'none', 500, 100, 200, 200)

        self.player.draw()

        pass

    def release(self):
        pass
